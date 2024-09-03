from telethon.sync import TelegramClient

from src.settings import (
    API_HASH,
    API_ID,
)

client = TelegramClient('parsing_lost_dogs', API_ID, API_HASH)


async def start_client():
    await client.start()
