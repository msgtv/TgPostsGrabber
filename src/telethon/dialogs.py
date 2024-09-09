import aiofiles

from typing import Iterable

from telethon.types import Channel

from src.telethon.start import client
from src.settings import DIALOGS_FILENAME
from src.utils import get_dialog_username


async def load_dialogs():
    async with aiofiles.open(DIALOGS_FILENAME, encoding='utf-8') as f:
        data = await f.read()

    data = data.strip()

    dialogs = []
    for row in data.split('\n'):
        dialog_id, title, username = row.split(':::')

        dialogs.append((int(dialog_id), title, username))

    return dialogs


async def save_dialogs(data):
    data_str = '\n'.join([':::'.join([str(x) for x in row]) for row in data])

    async with aiofiles.open(DIALOGS_FILENAME, 'w', encoding='utf-8') as f:
        await f.write(data_str)


async def get_entity_data(username):
    entity = await client.get_entity(username)
    if isinstance(entity, list):
        entity = entity[0]

    entity_id = isinstance(entity, Channel) and f'-100{entity.id}' or entity.id
    entity_data = (int(entity_id), entity.title, get_dialog_username(entity))

    return entity_data


# add_channel_to_analyze
async def add_channel_to_analyze(*usernames: Iterable[str]):
    data = await load_dialogs()
    added = []

    for username in usernames:
        try:
            entity_data = await get_entity_data(username)

            if entity_data not in data:
                added.append(entity_data)
                data.append(entity_data)

                yield f'Канал {entity_data[1]} успешно добавлен!'
            else:
                yield f'Канал {entity_data[1]} уже был добавлен!'
        except Exception as err:
            yield f'Ошибка! {err}'

    if added:
        await save_dialogs(data)


# reject_channel_from_analyze
async def reject_channel_from_analyze(*usernames: Iterable[str]):
    data = await load_dialogs()

    rejected = []

    for username in usernames:
        try:
            entity_data = await get_entity_data(username)

            if entity_data in data:
                rejected.append(entity_data)
                data.remove(entity_data)

                yield f'Канал "{entity_data[1]}" успешно исключен'
            else:
                yield f'Канала "{entity_data[1]}" нет в списке'
        except Exception as err:
            yield f'Ошибка! {err}'
    if rejected:
        await save_dialogs(data)

