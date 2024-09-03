from src.settings import DIALOGS_FILENAME


def load_dialogs():
    with open(DIALOGS_FILENAME, encoding='utf-8') as f:
        data = f.read().strip()

    dialogs = []
    for row in data.split('\n'):
        dialog_id, title, username = row.split(':::')

        dialogs.append((int(dialog_id), title, username))

    return dialogs
