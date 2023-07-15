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
from message_converter import convert_to_markdown, create_keyboard_markup


async def main():
    BOT_TOKEN = os.environ['TELEGRAM_BOT_TOKEN']

    bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
    dp = Dispatcher(storage=MemoryStorage())
    dp.include_router(router)

    async def on_message(message: AbstractIncomingMessage) -> None:
        json_body = json.loads(message.body)

        user_id = json_body["userInfo"]
        vacancy = json_body["vacancy"]

        keyboard = create_keyboard_markup(vacancy)
        await bot.send_message(user_id, convert_to_markdown(vacancy), reply_markup=keyboard, parse_mode="markdown")
        await message.ack()

    asyncio.create_task(rabbit.listen_for_new_vacancy(on_message))
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
