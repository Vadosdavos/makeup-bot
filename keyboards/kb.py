from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup

menu = [
    [InlineKeyboardButton(text="📚 Рекомендации по книге", callback_data="get_book_recommendations"),
    InlineKeyboardButton(text="🖼 Рекомендации по жанру ", callback_data="get_genre_recommendations")],
]
menu = InlineKeyboardMarkup(inline_keyboard=menu)
exit_kb = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="◀️ Выйти в меню")]], resize_keyboard=True)
iexit_kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="◀️ Выйти в меню", callback_data="menu")]])