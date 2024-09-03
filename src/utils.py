import os
import re


def get_dialog_username(dialog):
    entity = dialog.entity
    return entity.usernames and entity.usernames[0].username or entity.username


# def escape_markdown(text: str) -> str:
#     # Экранирование символов для MarkdownV2
#     escape_chars = r'_*[]()~`>#+-=|{}.!'
#     return re.sub(f"([{re.escape(escape_chars)}])", r'\\\1', text)

def escape_markdown(text):
    """функция для экранирования символов перед отправкой в маркдауне телеграма"""
    pattern = r"([_*\[\]()~|`-])"
    return re.sub(pattern, r"\\\1", text)


def create_dir_if_not_exists(path):
    if not os.path.isdir(path):
        os.makedirs(path)
