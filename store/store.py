from aiogram.fsm.state import StatesGroup, State

class PromptStore(StatesGroup):
    book_name = State()
    book_author = State()
    genre = State()