# ----------------------------------------------------------------------
# JSON-RPC API object
# ----------------------------------------------------------------------
# Copyright (C) 2007-2022 The NOC Project
# See LICENSE for details
# ----------------------------------------------------------------------

# Python modules
import asyncio
from collections import namedtuple
from typing import Optional

# Third-party modules
from fastapi import APIRouter, Header, HTTPException
from fastapi.responses import ORJSONResponse

# NOC modules
from noc.aaa.models.user import User
from noc.config import config
from noc.core.debug import error_report
from noc.core.error import NOCError
from noc.core.service.loader import get_service
from noc.core.service.models.jsonrpc import JSONRemoteProcedureCall, JSONRPCResponse
from noc.core.span import Span


Redirect = namedtuple("Redirect", ["location", "method", "params"])


class JSONRPCAPI(object):
    """
    JSON-RPC (specification 1.0) API implementation for FastAPI service
    https://www.jsonrpc.org/specification_v1
    """

    CALLING_SERVICE_HEADER = "X-NOC-Calling-Service"

    # API name for OpenAPI docs
    api_name = None
    # API description for OpenAPI docs
    api_description = None
    # Tags for OpenAPI docs
    openapi_tags = []
    # url-path for API endpoint (without closing /), e.g. /api/service_name
    url_path = None
    # Indicates whether the REMOTE-HTTP header is required in the request
    auth_required = False

    def __init__(self, router: APIRouter):
        self.service = get_service()
        self.logger = self.service.logger
        self.current_user = None
        self.router = router
        self.setup_routes()

    @classmethod
    def get_methods(cls):
        """
        Returns a list of available API methods
        """
        return [m for m in dir(cls) if getattr(getattr(cls, m), "api", False)]

    async def api_endpoint(
        self,
        req: JSONRemoteProcedureCall,
        remote_user: Optional[str] = Header(None, alias="Remote-User"),
        span_ctx: int = Header(0, alias="X-NOC-Span-Ctx"),
        span_id: int = Header(0, alias="X-NOC-Span"),
        calling_service: str = Header("unknown", alias=CALLING_SERVICE_HEADER),
    ):
        """
        Endpoint for FastAPI route.
        Execute selected API-method as method of JSONRPAPI child class instance
        """

        def get_current_user(remote_user):
            if not remote_user:
                if not self.auth_required:
                    return None
                else:
                    raise HTTPException(403, "Not authorized")
            user = User.get_by_username(remote_user)
            if not user:
                raise HTTPException(403, "Not authorized")
            if not user.is_active:
                raise HTTPException(403, "Not authorized")
            return user

        self.current_user = get_current_user(remote_user)
        if req.method not in self.get_methods():
            return {"error": f"Invalid method: '{req.method}'", "id": req.id}
        h = getattr(self, req.method)
        self.service.logger.debug(
            "[RPC call from %s] %s.%s(%s)", calling_service, self.api_name, req.method, req.params
        )
        in_label = None
        if config.features.forensic:
            lh = getattr(self, f"{req.method}_get_label", None)
            if lh:
                in_label = lh(*req.params)
        sample = 1 if span_ctx and span_id else 0
        with Span(
            server=self.service.name,
            service=f"api.{req.method}",
            sample=sample,
            parent=span_id,
            context=span_ctx,
            in_label=in_label,
        ) as span:
            try:
                if getattr(h, "executor", ""):
                    # Threadpool version
                    result = await self.service.run_in_executor(h.executor, h, *req.params)
                else:
                    # Serialized version
                    result = h(*req.params)
                if asyncio.isfuture(result) or asyncio.iscoroutine(result):
                    result = await result
                if isinstance(result, Redirect):
                    # Redirect protocol extension
                    return ORJSONResponse(
                        content={"method": result.method, "params": result.params, "id": req.id},
                        status_code=307,
                        headers={"location": result.location},
                    )
                else:
                    return ORJSONResponse(content={"result": result, "id": req.id})
            except NOCError as e:
                span.set_error_from_exc(e, e.code)
                error = f"Failed: {e}"
            except Exception as e:
                error_report()
                span.set_error_from_exc(e)
                error = f"Failed: {e}"
            return ORJSONResponse(content={"error": error, "id": req.id})

    def redirect(self, location, method, params):
        return Redirect(location=location, method=method, params=params)

    def setup_routes(self):
        """
        Setup FastAPI router by adding routes
        """
        for path in (self.url_path, f"{self.url_path}/"):
            self.router.add_api_route(
                path=path,
                endpoint=self.api_endpoint,
                methods=["POST"],
                response_model=JSONRPCResponse,
                tags=self.openapi_tags,
                name=self.api_name,
                description=self.api_description,
            )


def api(method):
    """
    API method decorator
    """
    method.api = True
    return method


def executor(name):
    """
    Denote API methods as been executed on threadpool executor

    @executor("script")
    @api
    def script(....)
    """

    def wrap(f):
        f.executor = name
        return f

    return wrap


class APIError(NOCError):
    pass
