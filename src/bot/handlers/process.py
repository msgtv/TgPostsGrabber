from aiogram.types import Message

from src.bot.keyboard import get_post_manage_kb


async def process_message_data(data_unit: dict[str, str], message: Message):
    if data_unit['state'] == 'end':
        await message.answer(
            text=data_unit['text']
        )
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
            text=f'Неизвестное состояние: {data_unit['text']}'
        )