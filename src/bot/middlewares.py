import traceback
from more_itertools import chunked

from aiogram import BaseMiddleware
from aiogram.types import (
    TelegramObject,
    Message,
)
from typing import Callable, Dict, Any, Awaitable

from src.settings import OWNER_ID, GROUP_CHAT_ID


class AuthMiddleware(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any]
    ) -> Any:
        chat_id = event.chat.id
        if chat_id not in (OWNER_ID, GROUP_CHAT_ID):
            return

        try:
            result = await handler(event, data)

            return result
        except Exception as err:
            err_string = (f"Что-то пошло не так: {err.__class__.__name__} - {err}"
                      f"Traceback: {traceback.format_exc()}")

            if isinstance(event, Message):
                for substring in chunked(err_string, 1000):
                    await event.answer(''.join(substring))

            print(
                err_string
            )
