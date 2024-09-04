from aiogram import Router
from aiogram.types import (
    Message,
)
from aiogram.filters import (
    CommandStart,
    Command
)

from src.bot.keyboard import (
    main_kb,
)

from src.bot.handlers.messages import start_grabbing

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
