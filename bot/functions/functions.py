import time
import asyncio
import difflib
from typing import Optional

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


async def check_unanswer_question():  # проверка неотвеченных вопросов раз в 5 мин
    while True:
        await asyncio.sleep(300)
        with db_question as connection:
            cursor = connection.cursor()
            data = cursor.execute('Select * From Questions')
            if not data:
                active_sups = cursor.execute('Select user_id From active_supports')
                for support in active_sups:
                    await bot.send_message(chat_id=support[0], text='Появились вопросы')


async def find_similar_question(user_question: str, threshold: float = 0.75):
    with db_answer as connection:
        cursor = connection.cursor()

        # Получаем все вопросы из базы
        cursor.execute('SELECT text_question, text_answer FROM answers')
        questions = {row[0]: row[1] for row in cursor.fetchall()}


        if not questions:
            return None

        # Ищем наиболее похожий вопрос
        best_match = None
        best_ratio = 0

        for question, answer in questions.items():
            # Используем SequenceMatcher для сравнения строк
            ratio = difflib.SequenceMatcher(None, user_question.lower(), question.lower()).ratio()

            if ratio > best_ratio and ratio >= threshold:
                best_ratio = ratio
                best_match = answer

        return best_match
