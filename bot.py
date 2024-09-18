import asyncio
import logging
from aiogram import Bot, Dispatcher
from config_reader import config
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from aiogram.types import FSInputFile

from handlers import meme, start, keltuzad_group
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
    dp.include_routers(start.router, meme.router, keltuzad_group.router)

    memes = await get_memes()
    kel_id = []
    kel_image = FSInputFile('assets/kel.jpg')

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, memes=memes, kel_image=kel_image, kel_id=kel_id)

if __name__ == "__main__":
    asyncio.run(main())