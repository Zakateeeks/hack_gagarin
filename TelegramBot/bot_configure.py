from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()
API_TOKEN = ""

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=storage)
