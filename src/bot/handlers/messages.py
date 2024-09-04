from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import (
    Message,
)

from src.bot.keyboard import get_post_manage_kb
from src.bot.btn_names import START_GRABBING, STATISTICS, RESET_STATS

from src.telethon.messages import get_unread_messages

router = Router()


@router.message(F.text == START_GRABBING)
async def start_grabbing(message: Message):
    await message.delete()

    async for data_unit in get_unread_messages():
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


@router.message(F.text == STATISTICS)
async def get_statistics(message: Message, state: FSMContext):
    await message.delete()

    data = await state.get_data()

    scores = data.get('scores', {1: 0, 2: 0, 3: 0})

    text = 'Текущая статистика\n\n'
    for k, v in scores.items():
        text += f'Карта №{k} - {v}\n'

    await message.answer(text=text)


@router.message(F.text == RESET_STATS)
async def reset_statistics(message: Message, state: FSMContext):
    await state.clear()

    await message.answer('Статистика успешно сброшена!')
