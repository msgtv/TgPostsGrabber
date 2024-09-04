from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import (
    Message,
)

from src.bot.handlers.process import process_message_data
from src.bot.btn_names import START_GRABBING, STATISTICS, RESET_STATS

from src.telethon.messages import get_unread_messages
from src.utils import delete_message_by_timer

router = Router()


@router.message(F.text == START_GRABBING)
async def start_grabbing(message: Message):
    await delete_message_by_timer(message)

    async for data_unit in get_unread_messages():
        await process_message_data(data_unit, message)


@router.message(F.text == STATISTICS)
async def get_statistics(message: Message, state: FSMContext):
    await delete_message_by_timer(message)

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
