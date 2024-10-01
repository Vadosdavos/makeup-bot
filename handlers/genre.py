from aiogram import Router, F, flags
from aiogram.types import Message, ReplyKeyboardRemove

from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from store.store import PromptStore
from utils.ai import generate_recommendation_by_genre
from aiogram.utils.formatting import Text, Bold, as_list, as_marked_list
from aiogram.types.callback_query import CallbackQuery 
from utils.text import set_genre, gen_wait, gen_error
from keyboards import kb

router = Router()

@router.callback_query(StateFilter(None), F.data == "get_genre_recommendations")
async def start_input_prompt(clbck: CallbackQuery, state: FSMContext):
    await clbck.message.answer(set_genre, reply_markup=kb.exit_kb)
    await state.set_state(PromptStore.genre)

@router.message(PromptStore.genre, F.text)
@flags.chat_action("typing")
async def get_genre_recommendations(message: Message, state: FSMContext):
    genre = message.text.lower()
    await state.clear()
    await message.answer(gen_wait, reply_markup=ReplyKeyboardRemove())
    res = await generate_recommendation_by_genre(genre)
    if not res:
        return await message.answer(gen_error, reply_markup=kb.iexit_kb)
    books_list = []
    for book in res:
        books_list.append(Text(Bold(book['title']), ' - ', f'{book['author']}. ', book['description'] ))
    content = as_list(f'Вот несколько книг из жанра "{genre}", которые обязательно стоит прочитать:', as_marked_list(*books_list, marker='📚'), "Надеюсь, эти рекомендации помогут вам найти новые интересные книги, которые вам понравятся!", sep="\n\n")

    return await message.answer(**content.as_kwargs())