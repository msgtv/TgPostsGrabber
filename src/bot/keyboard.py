from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
)

from src.bot.btn_names import START_GRABBING


main_kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text=START_GRABBING)],
], resize_keyboard=True)
