import sqlite3

from aiogram import types
from aiogram.filters import Command
from aiogram import Router
from loader import db, storage, dp

router = Router()


class User:
    def __init__(self, telegram_user_fullname, telegram_user_username, telegram_user_id):
        self.telegram_user_fullname = telegram_user_fullname
        self.telegram_user_username = telegram_user_username
        self.telegram_user_id = telegram_user_id


@router.message(Command('start'))
async def start_handler(msg: types.Message):
    await msg.answer(f'Привет, {msg.from_user.full_name}, я бот '
                     f'помощник разработанный для предприятия УСЗН. Напишите интересующий Вас вопрос:',
                     )

    telegram_user_id = msg.from_user.id
    telegram_user_username = msg.from_user.username
    telegram_user_fullname = msg.from_user.full_name
    user = User(telegram_user_fullname, telegram_user_username, telegram_user_id)
    await storage.set_data(user, [user])
    # with db as connection:
    #     cursor = connection.cursor()
    #     cursor.execute('''INSERT INTO Users (telegram_user_fullname,
    #     telegram_user_username, telegram_user_id) VALUES (?, ?, ?)''',
    #                    (user.telegram_user_fullname, user.telegram_user_username, user.telegram_user_id))
    #     connection.commit()
    #   раскоментить при продакте


# @router.message(IsSupport(storage.get_data(0)))
# async def start_handler(msg: types.Message):
#     await msg.answer('fgfgsad')
