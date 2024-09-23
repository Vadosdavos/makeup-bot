from aiogram import Router, F
from aiogram.types import Message

from middleware.chat_action import ChatActionMiddleware
from utils.ai import generate_recommendation

router = Router()
router.message.middleware(ChatActionMiddleware())

@router.message(F.text, flags={'long_operation': 'typing'})
async def cmd_book_recommendation(message: Message):
    prompt = message.text
    answer = await message.answer("Подбираю рекомендации...")
    res = await generate_recommendation(prompt)
    if res:
        return await answer.edit_text(res)
    else: 
        return await answer.edit_text("Error")
