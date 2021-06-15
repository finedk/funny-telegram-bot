from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from data.config import api_key

bot = Bot(token=api_key, parse_mode=types.ParseMode.HTML)
"""
    Тут можно изменить тип "storage" на MongoDB, RethinkDB, RedisDB, и др.
"""
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
