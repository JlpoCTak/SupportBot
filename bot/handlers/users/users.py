import asyncio
import sqlite3
import time

from aiogram import types
from aiogram.filters import Command
from aiogram import Router
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

from loader import db_question, db_answer
from bot.functions.functions import check_answer

router = Router()


class Actions(StatesGroup):
    usual = State()
    chatting = State()


class User:
    def __init__(self, telegram_user_fullname, telegram_user_username, telegram_user_id):
        self.telegram_user_fullname = telegram_user_fullname
        self.telegram_user_username = telegram_user_username
        self.telegram_user_id = telegram_user_id


@router.message(Command('start'))
async def start_handler(msg: types.Message, state: FSMContext):
    await msg.answer(f'Привет, {msg.from_user.full_name}, я бот '
                     f'помощник разработанный для предприятия УСЗН. Напишите интересующий Вас вопрос:',
                     )
    await state.set_state(Actions.chatting)
    telegram_user_id = msg.from_user.id
    telegram_user_username = msg.from_user.username
    telegram_user_fullname = msg.from_user.full_name
    user = User(telegram_user_fullname, telegram_user_username, telegram_user_id)
    # with db as connection:
    #     cursor = connection.cursor()
    #     cursor.execute('''INSERT INTO Users (telegram_user_fullname,
    #     telegram_user_username, telegram_user_id) VALUES (?, ?, ?)''',
    #                    (user.telegram_user_fullname, user.telegram_user_username, user.telegram_user_id))
    #     connection.commit()
    #   раскоментить при продакте


@router.message(Actions.chatting)
async def start_handler(msg: types.Message, state: FSMContext):
    with db_question as connection:
        cursor = connection.cursor()
        cursor.execute('INSERT Into Questions (user_id, msg_id, text_question) Values (?, ?, ?)',
                       (msg.from_user.id, msg.message_id, msg.text))
    await msg.answer('Дождитесь ответа')
    flag = True
    while flag:
        if await check_answer(msg.from_user.id, msg.message_id) is None:
            await asyncio.sleep(3)
            print('ждём')
        else:
            flag = False
            data = await check_answer(msg.from_user.id, msg.message_id)
            print('получаем данные')
            await msg.reply(text=data[4])
