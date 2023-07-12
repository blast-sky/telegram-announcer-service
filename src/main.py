import asyncio
import logging
import json
import os

from aio_pika.abc import AbstractIncomingMessage
from aiogram import Bot, Dispatcher
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

import rabbit
from handlers import router


async def main():
    BOT_TOKEN = os.environ['TELEGRAM_BOT_TOKEN']

    bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
    dp = Dispatcher(storage=MemoryStorage())
    dp.include_router(router)

    async def on_message(message: AbstractIncomingMessage) -> None:
        json_body = json.loads(message.body)
        await bot.send_message(json_body["userInfo"], str(json_body))

    asyncio.create_task(rabbit.listen_for_new_vacancy(on_message))
    # await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
