import asyncio
import logging
import requests
import random
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
from config_reader import config
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from aiogram.utils.formatting import Text, Bold, as_list, as_marked_section
from aiogram.types import URLInputFile, Message

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

memes = []

def get_memes():
    url = "https://api.imgflip.com/get_memes"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        global memes
        memes = data['data']['memes']
    else:
        print(f"Error: {response.status_code}")
    

@dp.message(Command("meme"))
async def cmd_meme(message: Message):
    random_int = random.randint(0, 99)
    meme = memes[random_int]
    image = URLInputFile(
        meme['url'],
        filename=meme['name']
    )
    await message.answer_photo(
        image,
        caption="Держи рандомный мемасик",
        show_caption_above_media=True
    )

# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: Message):
    content = as_list(
        Text("Привет, ",
        Bold(message.from_user.full_name), "!"),
        as_marked_section(
            Bold("В боте доступны команды:"),
            " /meme",
            marker='    '
        ),
        sep="\n\n"
    )
    await message.answer(**content.as_kwargs())

@dp.message()
async def cmd_keltuzad(message: Message):
    sub = 'ученые'
    text = message.text.lower()
    if sub in text:
        first_letter_index = text.index(sub)
        quote = f'{message.text[first_letter_index]}ченые'
        await message.answer('В говне моченые', reply_parameters={'message_id': message.message_id ,'quote': quote})

# Запуск процесса поллинга новых апдейтов
async def main():
    get_memes()
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())