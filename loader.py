import locale

from aiogram import Bot, types, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from envfileparser import get_env
from database import Database

locale.setlocale(locale.LC_ALL, get_env('LOCALE'))

bot = Bot(token=get_env('API_TOKEN'), parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
db = Database(f"database/{get_env('DB_NAME')}.db")
