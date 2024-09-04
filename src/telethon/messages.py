import os
from datetime import datetime, timedelta

from telethon.types import Message, MessageMediaPhoto, MessageMediaPoll
from telethon.errors import MessageIdInvalidError, ChatForwardsRestrictedError

from src.telethon.start import client
from src.telethon.dialogs import load_dialogs
from src.utils import get_dialog_username, delete_message_by_timer
from src.settings import PHOTOS_DIR

import time
import re


def is_private(dialog):
    if dialog.entity.username is not None:
        return False
    else:
        return True


def get_message_data(dialog, message):
    if all((not message.raw_text, not message.media or isinstance(message.media, MessageMediaPoll))):
        return {
            'state': 'end',
            'text': 'Пост является опросом или не имеет сообщений',
            'is_photos': False,
        }

    username = get_dialog_username(dialog)

    if username:
        post_url = f'https://t.me/{username}/{message.id}'
        # username = f'@{username}'
    else:
        post_url = f'https://t.me/c/{dialog.id}/{message.id}'

    message_text = f'<a href="{post_url}"><b>{dialog.title}</b></a>\n'
    # message_text += f'{username}\n\n' or ''

    is_media = bool(message.media)

    if not all((is_media, username)):
        message_text += f'{message.raw_text}'

    return {
        'state': 'process',
        'text': message_text,
        'is_photos': is_media,
    }


async def get_message_data_by_link(link):
    pat = r'https://t\.me/(c/)?(.*)/(\d+)'
    match = re.match(pat, link)

    _, username_or_id, message_id = match.groups()

    try:
        dialog = await client.get_entity(username_or_id)
        message = await client.get_messages(dialog, ids=int(message_id))

        data = get_message_data(dialog, message)

        return data
    except Exception as e:
        return {
            'state': 'end',
            'text': f'Ошибка!\n\n<b>{e.__class__.__name__}</b>\n{e}'
        }


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

            message_data = get_message_data(dialog.entity, message)
            if message_data is None:
                continue

            yield message_data

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
