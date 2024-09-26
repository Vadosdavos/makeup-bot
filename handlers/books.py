from aiogram import Router, F, flags
from aiogram.types import Message, ReplyKeyboardRemove

from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from store.store import Gen
from utils.ai import generate_recommendation
from aiogram.utils.formatting import Text, Bold, as_list, as_marked_list
from aiogram.types.callback_query import CallbackQuery 
from utils.text import set_book_name, set_book_author, gen_wait, gen_error
from keyboards import kb

router = Router()

@router.callback_query(StateFilter(None), F.data == "get_book_recommendations")
async def start_input_prompt(clbck: CallbackQuery, state: FSMContext):
    await clbck.message.answer(set_book_name, reply_markup=kb.exit_kb)
    await state.set_state(Gen.book_name)

@router.message(Gen.book_name, F.text)
async def book_name_accepted(message: Message, state: FSMContext):
    await state.update_data(book_name=message.text.lower())
    await message.answer(set_book_author)
    await state.set_state(Gen.book_author)

@router.message(Gen.book_author, F.text)
@flags.chat_action("typing")
async def get_book_recommendations(message: Message, state: FSMContext):
    user_prompt = await state.get_data()
    author = message.text
    prompt = f'{user_prompt['book_name']}, автор: {author.capitalize()}'
    await state.clear()
    answer = await message.answer(gen_wait, reply_markup=ReplyKeyboardRemove())
    res = await generate_recommendation(prompt)
    if not res:
        return await answer.edit_text(gen_error, reply_markup=kb.iexit_kb)
    books_list = []
    for book in res:
        books_list.append(Text(Bold(book['title']), ' - ', f'{book['author']}. ', book['description'] ))
    content = as_list(f'Если вам понравилась книга {prompt.capitalize()}, возможно, вам будут интересны следующие книги:', as_marked_list(*books_list, marker='📚'), "Надеюсь, эти рекомендации помогут вам найти новые интересные книги, которые вам понравятся!", sep="\n\n")

    return await message.answer(**content.as_kwargs())