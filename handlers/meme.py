from aiogram import Router
from aiogram.filters import Command
from aiogram.types import URLInputFile, Message
import random

router = Router()

@router.message(Command("meme"))
async def cmd_meme(message: Message, memes: list, memes_ids: dict):
    meme = random.choice(memes)
    meme_name = meme['name']
    if meme_name in memes_ids:
        await message.answer_photo(
            memes_ids[meme_name],
            caption="Держи рандомный мемасик",
            show_caption_above_media=True
        )
    else: 
        image = URLInputFile(
            meme['url'],
            filename=meme['name']
        )
        result = await message.answer_photo(
            image,
            caption="Держи рандомный мемасик",
            show_caption_above_media=True
        )
        memes_ids[meme_name] = result.photo[-1].file_id
