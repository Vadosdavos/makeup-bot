import asyncio
import logging
from aiogram import Bot, Dispatcher
from config_reader import config
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties

from handlers import keltuzad, meme, start
from utils.memes import get_memes

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)

async def main():
    bot = Bot(
            token=config.bot_token.get_secret_value(), 
            default=DefaultBotProperties(
            parse_mode=ParseMode.HTML
        ))
    dp = Dispatcher()
    dp.include_routers(start.router, meme.router, keltuzad.router)

    memes = await get_memes()

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, memes=memes)

if __name__ == "__main__":
    asyncio.run(main())