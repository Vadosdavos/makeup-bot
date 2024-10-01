import asyncio
import logging
from aiogram import Bot, Dispatcher
from utils.config_reader import config
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from aiogram.utils.chat_action import ChatActionMiddleware
from aiogram.fsm.storage.memory import MemoryStorage

from handlers import books, keltuzad, meme, start, genre
from utils.memes import get_memes

logging.basicConfig(level=logging.INFO)

async def main():
    bot = Bot(
            token=config.bot_token.get_secret_value(), 
            default=DefaultBotProperties(
            parse_mode=ParseMode.HTML
        ))
    dp = Dispatcher(storage=MemoryStorage())
    dp.message.middleware(ChatActionMiddleware())
    dp.include_routers(start.router, meme.router, books.router, genre.router, keltuzad.router)

    memes = await get_memes()
    memes_ids = {}

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, memes=memes, memes_ids=memes_ids)

if __name__ == "__main__":
    asyncio.run(main())