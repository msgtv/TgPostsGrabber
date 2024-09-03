from aiogram import F, Router
from aiogram.types import (
    Message,
)

from src.bot.btn_names import START_GRABBING

from src.telethon.messages import get_unread_messages

router = Router()


@router.message(F.text == START_GRABBING)
async def start_grabbing(message: Message):

    chat_id = message.chat.id

    async for text in get_unread_messages(chat_id):
        await message.answer(text=text)
