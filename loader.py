from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from data.config import *  # Import all configurations from the config module

import sqlite3

# Initialize the Telegram bot with the given token and parse mode set to HTML
bot = Bot(token=TOKEN)

# Initialize memory storage for the dispatcher
storage = MemoryStorage()

# Initialize the dispatcher with the memory storage
dp = Dispatcher(storage=storage)

# Initialize the SQLite database connection
db = sqlite3.connect('databases/database.db')
db_question = sqlite3.connect('databases/question.db')
db_answer = sqlite3.connect('databases/answers.db')

