#!./bin/python
# ---------------------------------------------------------------------
# MRTHandler
# ---------------------------------------------------------------------
# Copyright (C) 2007-2020 The NOC Project
# See LICENSE for details
# ---------------------------------------------------------------------

# Python modules
import logging
import asyncio
from typing import List

# Third-party modules
import orjson
from fastapi import APIRouter, Depends, Response

# NOC modules
from noc.aaa.models.user import User
from noc.core.service.loader import get_service
from noc.services.mrt.models.mrt import MRTScript
from noc.core.service.deps.user import get_current_user

from noc.core.service.error import RPCRemoteError, RPCError
from noc.core.perf import metrics
from noc.core.span import Span
from noc.sa.models.managedobject import ManagedObject
from noc.sa.models.useraccess import UserAccess
from noc.core.debug import error_report
from noc.core.error import ERR_UNKNOWN
from noc.config import config
from noc.core.comp import smart_text


logger = logging.getLogger(__name__)

router = APIRouter()


async def _write_chunk(res_list, obj):
    data = smart_text(orjson.dumps(obj))
    res_list.append("%s|%s" % (len(data), data))
    logger.debug("%s|%s" % (len(data), data))


async def _run_script(res_list, current_user, oid, script, args, span_id=0, bi_id=None):
    service = get_service()
    with Span(
        server="MRT",
        service="run_script",
        sample=int(config.mrt.enable_command_logging),
        in_label=bi_id or oid,
        parent=span_id,
        client=current_user,
    ) as span:
        try:
            await _write_chunk(res_list, {"id": str(oid), "running": True})
            logger.debug("[%s] Run script %s %s %s", span.context, oid, script, args)
            r = await service.sae.script(oid, script, args)
            metrics["mrt_success"] += 1
        except RPCRemoteError as e:
            span.set_error_from_exc(e, getattr(e, "remote_code", 1))
            return {"id": str(oid), "error": str(e)}
        except RPCError as e:
            logger.error("RPC Error: %s" % str(e))
            span.set_error_from_exc(e, getattr(e, "code", 1))
            return {"id": str(oid), "error": str(e)}
        except Exception as e:
            error_report()
            metrics["mrt_failed"] += 1
            span.set_error_from_exc(e)
            return {"id": str(oid), "error": str(e)}
        if script == "commands":
            if r["errors"]:
                span.set_error(ERR_UNKNOWN, r["output"])
                return {"id": str(oid), "error": r["output"]}
            span.out_label = r["output"]
            return {"id": str(oid), "result": r["output"]}
        else:
            return {"id": str(oid), "result": r}


@router.post("/api/mrt/")
async def api_mrt(req: List[MRTScript], current_user: User = Depends(get_current_user)):
    service = get_service()
    metrics["mrt_requests"] += 1
    # Disable nginx proxy buffering
    # self.set_header("X-Accel-Buffering", "no")
    # Object ids
    ids = set(int(d.id) for d in req if hasattr(d, "id") and hasattr(d, "script"))
    logger.info(
        "Run task on parralels: %d (Max concurrent %d), for User: %s",
        len(req),
        config.mrt.max_concurrency,
        current_user,
    )
    # Check access
    qs = ManagedObject.objects.filter(id__in=list(ids))
    if not current_user.is_superuser:
        adm_domains = UserAccess.get_domains(current_user)
        qs = qs.filter(administrative_domain__in=adm_domains)
    ids = dict(qs.values_list("id", "bi_id"))
    with Span(
        sample=int(config.mrt.enable_command_logging),
        server="MRT",
        service="post",
        client=current_user,
        in_label=req,
    ) as span:
        if service.use_telemetry:
            logger.info("[%s] Enable telemetry for task, user: %s", span.span_id, current_user)
        futures = set()
        res_list = []
        for d in req:
            if not hasattr(d, "id") or not hasattr(d, "script"):
                continue
            oid = int(d.id)
            if oid not in ids:
                await _write_chunk(res_list, {"id": str(d["id"]), "error": "Access denied"})
                metrics["mrt_access_denied"] += 1
                continue
            while len(futures) >= config.mrt.max_concurrency:
                done, futures = await asyncio.wait(futures, return_when=asyncio.FIRST_COMPLETED)
                for f in done:
                    r = await f
                    await _write_chunk(res_list, r)
            futures.add(
                _run_script(
                    res_list,
                    current_user,
                    oid,
                    d.script,
                    dict(d.args),
                    span_id=span.span_id,
                    bi_id=ids.get(oid),
                )
            )
        # Wait for rest
        while futures:
            done, futures = await asyncio.wait(futures, return_when=asyncio.FIRST_COMPLETED)
            for f in done:
                r = await f
                await _write_chunk(res_list, r)
    logger.info("Done")
    return Response(content=r"\n".join(res_list), media_type="text/html")
