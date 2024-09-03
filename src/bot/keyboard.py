from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardButton,
)

from src.bot.btn_names import START_GRABBING, DELETE_POST, CARD_NUMBERS, STATISTICS


main_kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text=START_GRABBING)],
    [KeyboardButton(text=STATISTICS)]
], resize_keyboard=True)


async def get_post_manage_kb(
        card_number: int = 0,
):
    kb = InlineKeyboardBuilder()

    for i in range(1, 4):
        btn_text = CARD_NUMBERS[i]
        callback_data = f'CardAdd_{i}'

        if i == card_number:
            btn_text = f'✅{btn_text}'
            callback_data = f'CardReject_{i}'

        kb.add(
            InlineKeyboardButton(
                text=btn_text,
                callback_data=callback_data,
            )
        )

    dlt_btn_callback_data = 'Delete'
    if card_number:
        dlt_btn_callback_data += f'_{card_number}'

    kb.add(
        InlineKeyboardButton(
            text=DELETE_POST,
            callback_data=dlt_btn_callback_data,
        )
    )

    return kb.adjust(4).as_markup()
