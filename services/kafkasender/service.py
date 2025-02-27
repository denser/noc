#!./bin/python
# ----------------------------------------------------------------------
# kafkasender service
# ----------------------------------------------------------------------
# Copyright (C) 2007-2023 The NOC Project
# See LICENSE for details
# ----------------------------------------------------------------------

# Python modules
import asyncio
import random
from typing import Optional

# Third-party modules
from aiokafka import AIOKafkaProducer
from aiokafka.errors import KafkaError, KafkaConnectionError
from kafka.errors import NodeNotReadyError

# NOC modules
from noc.config import config
from noc.core.service.fastapi import FastAPIService
from noc.core.perf import metrics
from noc.core.msgstream.message import Message
from noc.core.mx import MX_TO, MX_SHARDING_KEY, KAFKA_PARTITION
from noc.core.comp import smart_text


KAFKASENDER_STREAM = "kafkasender"


class KafkaSenderService(FastAPIService):
    name = "kafkasender"
    use_telemetry = True

    def __init__(self):
        super().__init__()
        self.producer: Optional[AIOKafkaProducer] = None

    async def on_activate(self):
        self.slot_number, self.total_slots = await self.acquire_slot()
        await self.subscribe_stream(
            KAFKASENDER_STREAM, self.slot_number, self.on_message, async_cursor=True
        )

    async def on_message(self, msg: Message) -> None:
        """
        Process incoming message. Usually forwarded by `mx` service.
        Message MUST have `To` header, containing target Kafka topic.
        Optional parameter 'Kafka_partition' can be specified.

        :param msg:
        :return:
        """
        metrics["messages"] += 1
        self.logger.debug("[%d] Receiving message %s", msg.offset, msg.headers)
        dst = msg.headers.get(MX_TO)
        if not dst:
            self.logger.debug("[%d] Missed '%s' header. Dropping", msg.offset, MX_TO)
            metrics["messages_drops"] += 1
            return
        await self.send_to_kafka(
            smart_text(dst),
            msg.value,
            msg.headers.get(MX_SHARDING_KEY),
            msg.headers.get(KAFKA_PARTITION),
        )
        metrics["messages_processed"] += 1

    async def send_to_kafka(
        self, topic: str, data: bytes, key: Optional[bytes] = None, partition: Optional[int] = None
    ) -> None:
        """
        Send data to kafka topic

        :param topic:
        :param data:
        :param key:
        :param partition:
        :return:
        """
        self.logger.debug("Sending to topic %s, partition: %s", topic, partition)
        producer = await self.get_producer()
        if partition is not None:
            partition = int(partition)
        try:
            await producer.send(topic, data, key=key, partition=partition)
            metrics["messages_sent_ok", ("topic", topic)] += 1
            metrics["bytes_sent", ("topic", topic)] += len(data)
        except KafkaError as e:
            metrics["messages_sent_error", ("topic", topic)] += 1
            self.logger.error("Failed to send to topic %s: %s", topic, e)
        except AttributeError as e:
            # Internal error
            metrics["messages_sent_error", ("topic", topic)] += 1
            self.logger.error("Fatal error when send message: %s", e)
            await self.producer.stop()
            self.producer = None

    async def get_producer(self) -> AIOKafkaProducer:
        """
        Returns connected kafka producer
        :return:
        """
        if self.producer:
            return self.producer
        bootstrap = [x.strip() for x in config.kafkasender.bootstrap_servers.split(",")]
        self.logger.info("Connecting to producer using bootstrap services %s", bootstrap)
        self.producer = AIOKafkaProducer(
            bootstrap_servers=bootstrap,
            acks=1,
            max_batch_size=config.kafkasender.max_batch_size,
            sasl_mechanism=config.kafkasender.sasl_mechanism,
            security_protocol=config.kafkasender.security_protocol,
            sasl_plain_username=config.kafkasender.username,
            sasl_plain_password=config.kafkasender.password,
            retry_backoff_ms=10000,
        )
        while True:
            try:
                self.logger.info("Try starting producer")
                await self.producer.start()
                break
            except (KafkaConnectionError, NodeNotReadyError) as e:
                # KafkaConnectionError: No connection to node with id 1
                metrics["errors", ("type", "kafka_producer_start")] += 1
                self.logger.error("Failed to connect producer: %s", e)
            await self._sleep_on_error(10)
        return self.producer

    @staticmethod
    async def _sleep_on_error(delay: float = 1.0, deviation: float = 0.5):
        """
        Wait random time on error.

        Args:
            delay: Average delay in seecods.
            deviation: Deviation from delay in seconds.
        """
        await asyncio.sleep(delay - deviation + 2 * deviation * random.random())


if __name__ == "__main__":
    KafkaSenderService().start()
