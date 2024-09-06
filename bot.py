import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from config_reader import config

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token=config.bot_token.get_secret_value())
# Диспетчер
dp = Dispatcher()

@dp.message(Command("scientists"))
async def cmd_test1(message: types.Message):
    await message.reply("Учёные - в говне мочёные")
    await message.answer_photo(photo='https://sun9-37.userapi.com/Rh37StG2J9-yPXPiWyXqm3g387BNiTSzMcxf_g/t9VCi31fdUo.jpg')


@dp.message(Command("info"))
async def cmd_info(message: types.Message, botName: str):
    await message.answer(f"Бот запущен с именем: {botName}")

# Хэндлер на команду /start
@dp.message()
async def cmd_start(message: types.Message):
    await message.answer("Привет! В боте доступны команды: /scientists, /info")

# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot, botName='Beauty bot')

if __name__ == "__main__":
    asyncio.run(main())