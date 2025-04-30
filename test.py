import sqlite3
import difflib
from typing import Optional


def test(user_question: str = 'кисточкой как красить', threshold: float = 0.5):
    db_answer = sqlite3.connect('databases/answers.db')
    conn = db_answer
    cursor = conn.cursor()

    # Получаем все вопросы из базы
    cursor.execute('SELECT text_question, text_answer FROM answers')
    questions = {row[0]: row[1] for row in cursor.fetchall()}

    conn.close()

    best_match = None
    best_ratio = 0

    for question, answer in questions.items():
        # Используем SequenceMatcher для сравнения строк
        ratio = difflib.SequenceMatcher(None, user_question.lower(), question.lower()).ratio()

        if ratio > best_ratio and ratio >= threshold:
            best_ratio = ratio
            best_match = {answer, ratio}

    print(best_match)


test()
