from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import configparser

config = configparser.ConfigParser()
config.read('../data.ini')
storage = MemoryStorage()
API_TOKEN = config["BOT"]["BOT_API"]

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=storage)
