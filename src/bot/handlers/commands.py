from itertools import islice
import json

# import pandas as pd
from aiogram import Router, Bot
from aiogram.types import (
    Message,
)
from aiogram.filters import (
    CommandStart,
    Command
)

# from src.chat_analyzer.parsing.parse_chat import (get_chat_df)
from src.bot.keyboard import (
    main_kb,
)
# from src.chat_analyzer.telethon import client
# from src.chat_analyzer.parsing.parse_chat import get_chat_new_messages, get_last_message_id
# from src.utils import (
#     str_date_to_datetime
# )

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    kb = main_kb
    await message.answer(
        'Salam popolam!',
        reply_markup=kb
    )
