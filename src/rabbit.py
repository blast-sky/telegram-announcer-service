import asyncio
import os
from typing import Callable, Awaitable

from aio_pika import connect
from aio_pika.abc import AbstractIncomingMessage

RABBIT_HOST = os.environ['RABBIT_HOST']


async def listen_for_new_vacancy(callback: Callable[[AbstractIncomingMessage], Awaitable]) -> None:
    connection = await connect(f"amqp://guest:guest@{RABBIT_HOST}")
    async with connection:
        channel = await connection.channel()
        queue = await channel.get_queue("hhsva.service.announcer.telegram")

        await queue.consume(callback, no_ack=False)
        await asyncio.Future()
