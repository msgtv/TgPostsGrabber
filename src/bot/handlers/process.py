import asyncio

import aiogram.exceptions
from aiogram.types import Message

from src.bot.keyboard import get_post_manage_kb
from src.utils import delete_message_by_timer


async def process_message_data(data_unit: dict[str, str], message: Message):
    async def send_message_data():
        if data_unit['state'] == 'end':
            msg = await message.answer(
                text=data_unit['text']
            )

            await delete_message_by_timer(msg, 30)

        elif data_unit['state'] == 'process':
            text = data_unit['text']
            is_have_photo = data_unit['is_photos']

            kb = await get_post_manage_kb()

            await message.answer(
                text=text,
                reply_markup=kb,
                disable_web_page_preview=not is_have_photo,
                disable_notification=True,
            )
        else:
            await message.answer(
                text=f'Неизвестное состояние: {data_unit['text']}',
            )

    while True:
        try:
            await send_message_data()
            break
        except aiogram.exceptions.TelegramRetryAfter as err:
            await asyncio.sleep(err.retry_after)
