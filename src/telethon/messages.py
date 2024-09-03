from datetime import datetime, timedelta
from src.telethon.start import client
from src.telethon.dialogs import load_dialogs

import time


def is_private(dialog):
    if dialog.entity.username is not None:
        return False
    else:
        return True


async def get_unread_messages():
    # now = datetime.now()
    # offset_date = now - timedelta(seconds=hours * 3600)
    dialogs_data = load_dialogs()
    dialog_ids = [d[0] for d in dialogs_data]

    dialogs = await client.get_dialogs()

    count = 0

    for dialog in dialogs:
        if dialog.id not in dialog_ids:
            continue

        unread_count = dialog.unread_count
        if unread_count == 0:
            continue

        messages = []

        async for message in client.iter_messages(
                dialog,
                limit=unread_count,
        ):
            if message.poll:
                continue
            messages.append(message.id)

            await client.send_read_acknowledge(
                entity=dialog,
                message=message
            )

        if len(messages) > 0:
            count += 1

        await client.forward_messages(
            entity=349385497,
            messages=messages,
            from_peer=dialog.id,
        )

        if count > 18:
            yield 'Сплю 30 секунд...'
            time.sleep(30)
            yield 'Продолжим!'
            count = 0

        yield f'Из {dialog.title} переслано {unread_count} сообщений'
