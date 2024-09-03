import os
import dotenv
from pathlib import Path

from collections import namedtuple


MODE = 'ENV'
BASE_DIR = './'

if MODE == 'ENV':
    BASE_DIR = Path(__file__).resolve().parent.parent

    ENV_FILE = BASE_DIR / r'.env'

    DATA_DIR = BASE_DIR / r'data'
    # RESULTS_DIR = BASE_DIR / 'results'
    # RESULTS_FILENAME = RESULTS_DIR / r'res.txt'
    #
    # CHATS_DIR = RESULTS_DIR / 'chats'
    # POLLS_DIR = RESULTS_DIR / r'polls'
    # HTML_RESULTS_DIR = RESULTS_DIR / r'html_chats'
    #
    # DAYS_JSON = BASE_DIR / r'days.json'
    #
    # ANALYZE_RESULTS_PICS = RESULTS_DIR / r'analyze_result_pics'
    # HTML_DIR = BASE_DIR / r'html'
    # STYLE_FILE = HTML_DIR / r'static/style.css'
else:
    ENV_FILE = './.env'

    DATA_DIR = f'{BASE_DIR}/data'

    # RESULTS_DIR = 'results'
    # RESULTS_FILENAME = f'{RESULTS_DIR}/res.txt'
    #
    # CHATS_DIR = f'{RESULTS_DIR}/chats'
    # POLLS_DIR = f'{RESULTS_DIR}/polls'
    # HTML_RESULTS_DIR = f'{RESULTS_DIR}/html_chats'
    #
    # DAYS_JSON = r'days.json'
    # ANALYZE_RESULTS_PICS = fr'{RESULTS_DIR}/analyze_result_pics'
    #
    # HTML_DIR = f'{BASE_DIR}/html'
    # STYLE_FILE = f'{HTML_DIR}/static/style.css'


dotenv.load_dotenv(ENV_FILE)

DIALOGS_FILENAME = os.path.join(DATA_DIR, 'dialogs')

# aiogram
API_TOKEN = os.getenv('API_TOKEN')

# telethon
API_HASH = os.getenv('API_HASH')
API_ID = os.getenv('API_ID')

# owner
OWNER_ID = int(os.getenv('OWNER_CHAT_ID'))
