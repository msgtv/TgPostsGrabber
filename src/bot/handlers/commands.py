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

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.delete()

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
