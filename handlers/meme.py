from aiogram import Router
from aiogram.filters import Command
from aiogram.types import URLInputFile, Message
import random

router = Router()

@router.message(Command("meme"))
async def cmd_meme(message: Message, memes: list):
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