import asyncio
import re

from aiogram import Router
from aiogram.types import (
    Message,
)
from aiogram.filters import (
    CommandStart,
    Command,
    CommandObject,
)

from src.bot.keyboard import (
    main_kb,
)

from src.bot.handlers.messages import start_grabbing
from src.bot.handlers.process import process_message_data
from src.telethon.messages import get_message_data_by_link
from src.telethon.dialogs import (
    add_channel_to_analyze,
    reject_channel_from_analyze
)
from src.utils import delete_message_by_timer

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await delete_message_by_timer(message)

    kb = main_kb
    await message.answer(
        'Salam popolam!',
        reply_markup=kb
    )


@router.message(Command('grab'))
async def cmd_grab(message: Message):
    await start_grabbing(message)


@router.message(Command('getpost'))
async def cmd_get_post(message: Message, command: CommandObject):
    await delete_message_by_timer(message)

    command_args = re.split(r'\s+', command.args)

    if not command_args:
        await message.answer(
            text='Не обнаружена ссылка на пост!\n'
                 'Пример команды: /getpost <ссылка на пост/сообщение>'
        )
    else:
        for post_link in command_args:
            # получить посты и отправить в получателю
            message_data = await get_message_data_by_link(post_link)
            await process_message_data(message_data, message)


@router.message(Command('addchannel'))
async def cmd_add_channel(message: Message, command: CommandObject):
    await delete_message_by_timer(message)

    if not command.args:
        await message.answer(
            text='Не обнаружены username или id канала\n'
                 'Пример команды: /addchannel <username/id>'
        )
    else:
        usernames = re.split(r'\s+', command.args)
        async for text in add_channel_to_analyze(*usernames):
            new_msg = await message.answer(text)
            await delete_message_by_timer(new_msg)


@router.message(Command('rejectchannel'))
async def cmd_add_channel(message: Message, command: CommandObject):
    await delete_message_by_timer(message)

    if not command.args:
        await message.answer(
            text='Не обнаружены username или id канала\n'
                 'Пример команды: /addchannel <username/id>'
        )
    else:
        usernames = re.split(r'\s+', command.args)

        async for text in reject_channel_from_analyze(*usernames):
            new_msg = await message.answer(text)
            await delete_message_by_timer(new_msg)
