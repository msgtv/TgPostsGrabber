import os
import dotenv
from pathlib import Path
from src.utils import create_dir_if_not_exists


MODE = 'ENV'
BASE_DIR = './'

if MODE == 'ENV':
    BASE_DIR = Path(__file__).resolve().parent.parent

    ENV_FILE = BASE_DIR / r'.env'

    DATA_DIR = BASE_DIR / r'data'
else:
    ENV_FILE = './.env'

    DATA_DIR = f'{BASE_DIR}/data'


dotenv.load_dotenv(ENV_FILE)

DIALOGS_FILENAME = os.path.join(DATA_DIR, 'dialogs')
PHOTOS_DIR = os.path.join(DATA_DIR, 'photos')

# aiogram
API_TOKEN = os.getenv('API_TOKEN')

# telethon
API_HASH = os.getenv('API_HASH')
API_ID = os.getenv('API_ID')

# owner
OWNER_ID = int(os.getenv('OWNER_CHAT_ID'))

# group
GROUP_CHAT_ID = int(os.getenv('GROUP_CHAT_ID'))

# Создать папки, если не существуют
for d in (
        DATA_DIR,
        PHOTOS_DIR,
):
    create_dir_if_not_exists(d)
