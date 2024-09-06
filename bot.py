import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
from config_reader import config
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from aiogram.utils.formatting import Text, Bold, as_list, as_marked_section

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(
        token=config.bot_token.get_secret_value(), 
        default=DefaultBotProperties(
        parse_mode=ParseMode.HTML
    ))
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
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    content = as_list(
        Text("Привет, ",
        Bold(message.from_user.full_name), "!"),
        as_marked_section(
            Bold("В боте доступны команды:"),
            " /scientists",
            "/info",
            marker='    '
        ),
        sep="\n\n"
    )
    await message.answer(**content.as_kwargs())

# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot, botName='Beauty bot')

if __name__ == "__main__":
    asyncio.run(main())