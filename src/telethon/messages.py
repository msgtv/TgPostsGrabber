import os
from datetime import datetime, timedelta

from telethon.types import Message, MessageMediaPhoto
from telethon.errors import MessageIdInvalidError, ChatForwardsRestrictedError

from src.telethon.start import client
from src.telethon.dialogs import load_dialogs
from src.utils import get_dialog_username, escape_markdown
from src.settings import PHOTOS_DIR

import time


def is_private(dialog):
    if dialog.entity.username is not None:
        return False
    else:
        return True


def is_have_photo(message: Message):
    return message.media and isinstance(message.media, MessageMediaPhoto)


async def get_unread_messages():
    dialogs_data = load_dialogs()
    dialog_ids = [d[0] for d in dialogs_data]

    dialogs = await client.get_dialogs()

    total_messages = 0

    state = 'process'

    for dialog in dialogs:
        if dialog.id not in dialog_ids:
            continue

        unread_count = dialog.unread_count
        if unread_count == 0:
            continue

        async for message in client.iter_messages(
                dialog,
                limit=unread_count,
        ):
            await client.send_read_acknowledge(
                entity=dialog,
                message=message
            )

            if message.poll or not message.raw_text:
                continue

            username = get_dialog_username(dialog)

            if username:
                post_url = f'https://t.me/{username}/{message.id}'
                username = f'@{username}'
            else:
                post_url = f'https://t.me/c/{dialog.entity.id}/{message.id}'

            message_text = f'<a href="{post_url}">{dialog.title}</a>\n'
            # message_text += f'{username}\n\n' or ''

            is_media = bool(message.media)

            if not all((is_media, username)):
                message_text += f'{message.raw_text}'

            yield {
                'state': state,
                'text': message_text,
                'is_photos': is_media,
            }

            total_messages += 1

    state = 'end'
    if total_messages:
        message_text = f'Чатов: {len(dialog_ids)}\nСобрано {total_messages} новых постов'
    else:
        message_text = f'Чатов: {len(dialog_ids)}\nНовых постов не обнаружено!'

    yield {
        'state': state,
        'text': message_text
    }
