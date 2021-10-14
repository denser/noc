#!./bin/python
# ----------------------------------------------------------------------
# datastream service
# ----------------------------------------------------------------------
# Copyright (C) 2007-2020 The NOC Project
# See LICENSE for details
# ----------------------------------------------------------------------

# Python modules
import threading
import time
import random
from queue import Queue, Empty
import asyncio

# Third-party modules
import pymongo.errors

# NOC modules
from noc.core.service.tornado import TornadoService
from noc.services.datastream.handler import DataStreamRequestHandler
from noc.core.datastream.loader import loader
from noc.config import config


class DataStreamService(TornadoService):
    name = "datastream"
    use_mongo = True
    if config.features.traefik:
        traefik_backend = "datastream"
        traefik_frontend_rule = "PathPrefix:/api/datastream"

    def __init__(self):
        super().__init__()
        self.ds_queue = {}

    def get_datastreams(self):
        r = []
        for name in loader:
            if not getattr(config.datastream, "enable_%s" % name, False):
                continue
            ds = loader[name]
            if ds:
                self.logger.info("[%s] Initializing datastream", name)
                r += [ds]
            else:
                self.logger.info("[%s] Failed to initialize datastream", name)
        return r

    def get_handlers(self):
        return [
            (
                r"/api/datastream/%s" % ds.name,
                DataStreamRequestHandler,
                {"service": self, "datastream": ds},
            )
            for ds in self.get_datastreams()
        ]

    async def on_activate(self):
        # Detect we have working .watch() implementation
        if self.has_watch():
            has_watch = True
        else:
            self.logger.warning(
                "Realtime change tracking is not available, using polling emulation."
            )
            has_watch = False
        # Start watcher threads
        self.ds_queue = {}
        for ds in self.get_datastreams():
            if has_watch and getattr(config.datastream, "enable_%s_wait" % ds.name):
                waiter = self.watch_waiter
            else:
                waiter = self.sleep_waiter
            self.logger.info("Starting %s waiter thread", ds.name)
            queue = Queue()
            self.ds_queue[ds.name] = queue
            thread = threading.Thread(
                target=waiter, args=(ds.get_collection(), queue), name="waiter-%s" % ds.name
            )
            thread.setDaemon(True)
            thread.start()

    def has_watch(self):
        """
        Detect cluster has working .watch() implementation

        :return: True if .watch() is working
        """
        # Get one datastream collection
        dsn = next(loader.iter_classes())
        ds = loader[dsn]
        coll = ds.get_collection()
        # Check pymongo has .watch
        if not hasattr(coll, "watch"):
            self.logger.error("pymongo does not support .watch() method")
            return False
        # Check connection is member of replica set
        if not config.mongo.rs:
            self.logger.error("MongoDB must be in replica set mode to use .watch()")
            return False
        # Check version, MongoDB 3.6.0 or later required
        client = coll.database.client
        sv = tuple(int(x) for x in client.server_info()["version"].split("."))
        if sv < (3, 6, 0):
            self.logger.error("MongoDB 3.6 or later require to use .watch()")
            return False
        return True

    def _run_callbacks(self, queue):
        """
        Execute callbacks from queue
        :param queue:
        :return:
        """
        while True:
            try:
                cb = queue.get(block=False)
            except Empty:
                break
            cb(self.loop)

    def watch_waiter(self, coll, queue):
        """
        Waiter thread tracking mongo's ChangeStream
        :param coll:
        :param queue:
        :return:
        """
        while True:
            with coll.watch(
                pipeline=[{"$project": {"_id": 1}}],
                max_await_time_ms=config.datastream.max_await_time_ms * 1_000,
            ) as stream:
                try:
                    for _ in stream:
                        # Change received, call all pending callback
                        self._run_callbacks(queue)
                except pymongo.errors.PyMongoError as e:
                    self.logger.error("Unrecoverable watch error: %s", e)
                    time.sleep(1)

    def sleep_waiter(self, coll, queue):
        """
        Simple timeout waiter
        :param coll:
        :param queue:
        :return:
        """
        TIMEOUT = 60
        JITER = 0.1
        while True:
            # Sleep timeout is random of [TIMEOUT - TIMEOUT * JITTER, TIMEOUT + TIMEOUT * JITTER]
            time.sleep(TIMEOUT + (random.random() - 0.5) * TIMEOUT * 2 * JITER)
            self._run_callbacks(queue)

    async def wait(self, ds_name):
        def notify(loop):
            loop.call_soon(event.set)
            # asyncio.get_running_loop().call_soon(event.set)

        if ds_name not in self.ds_queue:
            return
        event = asyncio.Event()
        self.ds_queue[ds_name].put(notify)
        await event.wait()


if __name__ == "__main__":
    DataStreamService().start()
