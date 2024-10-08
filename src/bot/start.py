from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

import asyncio

from src.settings import API_TOKEN
from src.bot.middlewares import AuthMiddleware
from src.bot.handlers import commands
from src.bot.handlers import messages
from src.bot.handlers import callbacks

from aiogram.client.bot import DefaultBotProperties
from aiogram.enums import ParseMode

bot = Bot(
    token=API_TOKEN,
    default=DefaultBotProperties(
        parse_mode=ParseMode.HTML
    )
)

dp = Dispatcher(storage=MemoryStorage())

dp.include_router(commands.router)
dp.include_router(messages.router)
dp.include_router(callbacks.router)
dp.message.middleware(AuthMiddleware())


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
