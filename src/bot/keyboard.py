from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    ReplyKeyboardMarkup,
    KeyboardButton,
)

from src.bot.btn_names import (
    START_GRABBING,
    CANCEL_BTN_NAME,
)


main_kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text=START_GRABBING)],
], resize_keyboard=True)
