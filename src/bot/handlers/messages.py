import os
from datetime import datetime

from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import (
    FSInputFile,
    Message,
    InlineKeyboardMarkup,
)

from src.bot.states import ParsingParamsState
from src.bot.btn_names import START_GRABBING

from src.telethon.messages import get_unread_messages

router = Router()


@router.message(F.text == START_GRABBING)
async def start_game(message: Message, state: FSMContext):
    # начать сбор непрочитанных постов со всех каналов
    # await state.set_state(ParsingParamsState.hours)
    #
    # await message.answer(text='Введите количество часов')

    async for text in get_unread_messages():
        # await message.bot.forward_messages(
        #     chat_id=message.from_user.id,
        #     from_chat_id=chat_id,
        #     message_ids=message_ids
        # )
        await message.answer(text=text)


# @router.message(ParsingParamsState.hours)
# async def get_hours_count(message: Message, state: FSMContext):
#     # hours = float(message.text)
#     # await state.clear()
#
#     # начать парсинг сообщений, непрочитанных
#     # за последние hours часов
#
#     async for chat_name, num in get_unread_messages():
#         # await message.bot.forward_messages(
#         #     chat_id=message.from_user.id,
#         #     from_chat_id=chat_id,
#         #     message_ids=message_ids
#         # )
#         await message.answer(text=f'Из {chat_name} переслано {num} сообщений')
