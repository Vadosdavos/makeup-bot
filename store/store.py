from aiogram.fsm.state import StatesGroup, State

class Gen(StatesGroup):
    book_name = State()
    book_author = State()