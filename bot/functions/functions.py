import time
import asyncio

from loader import db_question, db_answer
from time import sleep
from loader import bot


async def check_answer(user_id, msg_id):
    with db_answer as connection:
        cursor = connection.cursor()
        data = cursor.execute('Select * From answers Where user_id = ? And msg_id = ?',
                              (user_id, msg_id,)).fetchone()
        if not data:
            return None
        else:
            return data


async def check_unanswer_question():    #проверка неотвеченных вопросов раз в 5 мин
    while True:
        await asyncio.sleep(300)
        with db_question as connection:
            cursor = connection.cursor()
            data = cursor.execute('Select * From Questions')
            if data:
                active_sups = cursor.execute('Select user_id From active_supports')
                for support in active_sups:
                    await bot.send_message(chat_id=support[0], text='Появились вопросы')

