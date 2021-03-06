import asyncio
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from glQiwiApi import QiwiWrapper

from data import config
from data.config import API_ACCESS_TOKEN, PHONE_NUMBER, SecretP2
from utils.db_api.database import Database

bot = Bot(token=config.BOT_TOKEN, parse_mode="Markdown")
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
loop = asyncio.get_event_loop()
db = loop.run_until_complete(Database.create())
wallet = QiwiWrapper(api_access_token=API_ACCESS_TOKEN, phone_number=PHONE_NUMBER, secret_p2p=SecretP2)
