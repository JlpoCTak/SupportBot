import datetime
import os
import sqlite3


def admin() -> int:
    '''
    Taker id of Super admin
    :return: Int(telegram_user_id) of Super admin
    '''
    with sqlite3.connect('./databases/database.db') as connection:
        cursor = connection.cursor()
        id = int(cursor.execute('Select telegram_user_id from Superadmin').fetchall()[0][0])
        return id


def support() -> int:
    '''
        Taker id of Support
        :return: Int(telegram_user_id) of Support
        '''
    with sqlite3.connect('./databases/database.db') as connection:
        cursor = connection.cursor()
        id = cursor.execute('Select telegram_user_id from Superadmin').fetchall()[0][0]
        return id


TOKEN = os.getenv('TOKEN')
ADMIN = admin()
