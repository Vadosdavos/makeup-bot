from aiogram import Router, F
from aiogram.types import Message

from middleware.chat_action import ChatActionMiddleware
from utils.ai import generate_recommendation
from aiogram.utils.formatting import Text, Bold, as_list, as_marked_list

router = Router()
router.message.middleware(ChatActionMiddleware())

@router.message(F.text, flags={'long_operation': 'typing'})
async def get_book_recommendations(message: Message):
    prompt = message.text
    answer = await message.answer("Подбираю рекомендации...")
    res = await generate_recommendation(prompt)
    books_list = []
    for book in res:
        books_list.append(Text(Bold(book['title']), ' - ', f'{book['author']}. ', book['description'] ))
    content = as_list(f'Если вам понравилась {prompt}, возможно, вам будут интересны следующие книги:', as_marked_list(*books_list, marker='📚'), "Надеюсь, эти рекомендации помогут вам найти новые интересные книги, которые вам понравятся!", sep="\n\n")
    if res:
        return await answer.edit_text(**content.as_kwargs())
    else: 
        return await answer.edit_text("Error")
