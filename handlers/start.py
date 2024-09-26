from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove
from utils.text import greet, menu, cancel
from keyboards import kb
from aiogram.fsm.context import FSMContext

router = Router()

@router.message(Command("start"))
async def cmd_start(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(greet.format(name=message.from_user.full_name), reply_markup=kb.menu)

@router.message(Command(commands=["cancel"]))
@router.message(F.text == "Меню")
@router.message(F.text == "◀️ Выйти в меню")
async def back_to_menu(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(cancel, reply_markup=ReplyKeyboardRemove())
    await message.answer(menu, reply_markup=kb.menu)