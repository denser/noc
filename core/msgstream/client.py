# ----------------------------------------------------------------------
# MsgStream Client
# ----------------------------------------------------------------------
# Copyright (C) 2007-2022 The NOC Project
# See LICENSE for details
# ----------------------------------------------------------------------

# Python modules
import logging
from typing import Optional, Dict, AsyncIterable, Any

# Third-party modules
import orjson

# NOC modules
from noc.core.handler import get_handler
from .message import Message, PublishRequest
from .config import get_stream
from .metadata import Metadata, PartitionMetadata
from noc.config import config


logger = logging.getLogger(__name__)


class MessageStreamClient(object):
    """
    Client for Message Stream application (like Kafka)
    1. Access Messages
      * publish
      * subscribe
    2. Migration
      * Ensure Stream
    3. Processed Exception
      *
    4. Cursor API
      * fetch cursor
      * set cursor
    ? Namespace
    ? MessageQueueBuffer (SaveHeaders)
    """

    def __init__(self):
        self.client = self.get_client()

    @classmethod
    def get_client(cls) -> "MessageStreamClient":
        logger.debug("Using MsgStream client backend: %s", config.msgstream.client_class)
        c = get_handler(config.msgstream.client_class)
        if c:
            return c()
        logger.error("Cannot load MsgStream client")
        raise NotImplementedError("Cannot load MsgStream client")

    async def __aenter__(self) -> "MessageStreamClient":
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.client.close()

    async def subscribe(
        self,
        stream: str,
        partition: Optional[int] = None,
        start_offset: Optional[int] = None,
        start_timestamp: Optional[float] = None,
        resume: bool = False,
        cursor_id: Optional[str] = None,
        timeout: Optional[int] = None,
        allow_isr: bool = False,
    ) -> AsyncIterable[Message]:
        async for msg in self.client.subscribe(
            stream=stream,
            partition=partition,
            start_offset=start_offset,
            start_timestamp=start_timestamp,
            resume=resume,
            cursor_id=cursor_id,
            timeout=timeout,
        ):
            yield msg

    async def publish(
        self,
        value: bytes,
        stream: Optional[str] = None,
        key: Optional[bytes] = None,
        partition: Optional[int] = None,
        headers: Optional[Dict[str, bytes]] = None,
        wait_for_stream: bool = False,
    ) -> None:
        # Build message
        await self.client.publish(
            value,
            stream=stream,
            key=key,
            partition=partition,
            headers=headers,
            wait_for_stream=wait_for_stream,
        )

    async def publish_request(self, req: PublishRequest, wait_for_stream: bool = False):
        await self.publish(
            req.data,
            stream=req.stream,
            key=req.key,
            partition=req.partition,
            headers=req.headers,
            wait_for_stream=wait_for_stream,
        )

    async def fetch_metadata(
        self, stream: Optional[str] = None, wait_for_stream: bool = False
    ) -> Metadata:
        return await self.client.fetch_metadata(stream, wait_for_stream=wait_for_stream)

    async def fetch_partition_metadata(
        self, stream: str, partition: int, wait_for_stream: bool = False
    ) -> PartitionMetadata:
        r = await self.fetch_metadata(stream)
        return r.metadata[stream][partition]

    async def create_stream(
        self,
        name: str,
        group: Optional[str] = None,
        partitions: int = 0,
        replication_factor: int = 0,
    ) -> None:
        """
        Create Stream by settings
        :param name:
        :param group:
        :param partitions:
        :param replication_factor:
        :return:
        """
        await self.client.create_stream(
            name=name,
            group=group,
            partitions=partitions,
            replication_factor=replication_factor,
        )

    async def delete_stream(self, name: str) -> None:
        await self.client.delete_stream(name)

    @classmethod
    def get_replication_factor(cls, meta) -> int:
        return min(len(meta.brokers), 2)

    async def ensure_stream(self, name: str, partitions: Optional[int] = None) -> bool:
        """
        Ensure stream settings
        :param name:
        :param partitions:
        :return:
        """
        # Get stream config
        s = get_stream(name)
        # Get liftbridge metadata
        partitions = partitions or s.get_partitions()
        # Check if stream is configured properly
        if not partitions:
            logger.info("Stream '%s' without partition. Skipping..", name)
            return False
        meta = await self.fetch_metadata(name)
        rf = self.client.get_replication_factor(meta)
        stream_meta = meta.metadata[name] if name in meta.metadata else None
        if stream_meta and len(stream_meta) == partitions:
            return False
        elif stream_meta:
            # Alter settings
            logger.info(
                "Altering stream %s due to partition/replication factor mismatch (%d -> %d)",
                name,
                len(stream_meta),
                partitions,
            )
            return await self.alter_stream(
                name, stream_meta, new_partitions=partitions, replication_factor=rf
            )
        logger.info("Creating stream %s with %s partitions", name, partitions)
        await self.create_stream(name, partitions=partitions, replication_factor=rf)
        return True

    async def fetch_cursor(self, stream: str, partition: int, cursor_id: str) -> int:
        """
        Getting stream cursor value
        :param stream:
        :param partition:
        :param cursor_id:
        :return:
        """
        return await self.client.fetch_cursor(stream, partition, cursor_id)

    async def set_cursor(self, stream: str, partition: int, cursor_id: str, offset: int) -> None:
        """
        Set stream cursor value
        :param stream:
        :param partition:
        :param cursor_id:
        :param offset:
        :return:
        """
        await self.client.set_cursor(stream, partition, cursor_id, offset=offset)

    @staticmethod
    def get_publish_request(
        data: Any,
        stream: str,
        partition: Optional[int] = None,
        headers: Optional[Dict[str, bytes]] = None,
        sharding_key: int = 0,
    ) -> PublishRequest:
        """
        Build message

        :param data: Data for transmit
        :param stream: Message type
        :param headers: additional message headers
        :param sharding_key: Key for sharding
        :param partition: Partition for send
        :return:
        """
        if not isinstance(data, bytes):
            data = orjson.dumps(data)
        return PublishRequest(
            data=data,
            stream=stream,
            partition=partition,
            key=sharding_key,
            headers=headers,
        )

    async def alter_stream(
        self,
        name: str,
        current_meta: Dict[int, PartitionMetadata],
        new_partitions: Optional[int] = None,
        replication_factor: Optional[int] = None,
    ) -> bool:
        old_partitions = len(current_meta)
        n_msg: Dict[int, int] = {}  # partition -> copied messages
        s = get_stream(name)
        logger.info("Altering stream %s", name)
        # Create temporary stream with same structure, as original one
        tmp_stream = f"__tmp-{name}"
        logger.info("Creating temporary stream %s", tmp_stream)
        await self.delete_stream(tmp_stream)
        await self.create_stream(
            name=tmp_stream,
            partitions=old_partitions,
            replication_factor=1,
        )
        # Copy all unread data to temporary stream as is
        for partition in range(old_partitions):
            logger.info("Copying partition %s:%s to %s:%s", name, partition, tmp_stream, partition)
            n_msg[partition] = 0
            # Get current offset
            p_meta = await self.fetch_partition_metadata(name, partition)
            newest_offset = p_meta.newest_offset or 0
            # Fetch cursor
            current_offset = (
                await self.fetch_cursor(
                    stream=name,
                    partition=partition,
                    cursor_id=s.cursor_name,
                )
                or 0
            )
            # For -1 as nothing messages
            current_offset = max(0, current_offset)
            if current_offset > newest_offset:
                # Fix if cursor not set properly
                current_offset = newest_offset
            logger.info(
                "Start copying from current_offset: %s to newest offset: %s",
                current_offset,
                newest_offset,
            )
            if current_offset < newest_offset:
                async for msg in self.subscribe(
                    stream=name, partition=partition, start_offset=current_offset
                ):
                    await self.publish(
                        msg.value,
                        stream=tmp_stream,
                        partition=partition,
                    )
                    n_msg[partition] += 1
                    if msg.offset == newest_offset:
                        break
            if n_msg[partition]:
                logger.info("  %d messages has been copied", n_msg[partition])
            else:
                logger.info("  nothing to copy")
        # Drop original stream
        logger.info("Dropping original stream %s", name)
        await self.delete_stream(name)
        # Create new stream with required structure
        logger.info("Creating stream %s", name)
        await self.create_stream(
            name=name,
            partitions=new_partitions,
            replication_factor=replication_factor,
        )
        # Copy data from temporary stream to a new one
        for partition in range(old_partitions):
            logger.info("Restoring partition %s:%s to %s" % (tmp_stream, partition, new_partitions))
            # Re-route dropped partitions to partition 0
            dest_partition = partition if partition < new_partitions else 0
            n = n_msg[partition]
            if n > 0:
                async for msg in self.subscribe(
                    stream=tmp_stream,
                    partition=partition,
                    start_offset=0,
                ):
                    await self.publish(msg.value, stream=name, partition=dest_partition)
                    n -= 1
                    if not n:
                        break
                logger.info("  %s messages restored", n_msg[partition])
            else:
                logger.info("  nothing to restore")
        # Drop temporary stream
        logger.info("Dropping temporary stream %s", tmp_stream)
        await self.delete_stream(tmp_stream)
        # Uh-oh
        logger.info("Stream %s has been altered", name)
        return True
