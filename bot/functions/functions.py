from loader import db_question, db_answer


async def check_answer(user_id, msg_id):
    with db_answer as connection:
        cursor = connection.cursor()
        data = cursor.execute('Select * From answers Where user_id = ? And msg_id = ?',
                              (user_id, msg_id,)).fetchone()
        if not data:
            return None
        else:
            return data
