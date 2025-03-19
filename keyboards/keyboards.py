from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

language_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Английский"), KeyboardButton(text="Немецкий")]
    ],
    resize_keyboard=True
)