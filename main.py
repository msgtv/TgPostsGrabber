import asyncio
import logging

from src.telethon.start import start_client as start_telethon
from src.bot.start import dp, bot


async def start():
    await start_telethon()
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(start())


