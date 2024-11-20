import sqlite3


def user_db():
    connection = sqlite3.connect('databases/database.db')
    cursor = connection.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users (
    id INTEGER PRIMARY KEY,
    telegram_user_fullname TEXT NOT NULL,
    telegram_user_username TEXT NOT NULL,
    telegram_user_id TEXT NOT NULL
    )
    ''')
    connection.commit()
    connection.close()


def support_db():
    connection = sqlite3.connect('databases/database.db')
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Supports (
        id INTEGER PRIMARY KEY,
        telegram_user_fullname TEXT NOT NULL,
        telegram_user_username TEXT NOT NULL,
        telegram_user_id TEXT NOT NULL
        )
        ''')
    connection.commit()
    connection.close()


def admin_db():
    connection = sqlite3.connect('databases/database.db')
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Admins (
        id INTEGER PRIMARY KEY,
        telegram_user_fullname TEXT NOT NULL,
        telegram_user_username TEXT NOT NULL,
        telegram_user_id TEXT NOT NULL
        )
        ''')
    connection.commit()
    connection.close()


def superadmin_db():
    connection = sqlite3.connect('databases/database.db')
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Superadmin (
        id INTEGER PRIMARY KEY,
        telegram_user_fullname TEXT NOT NULL,
        telegram_user_username TEXT NOT NULL,
        telegram_user_id TEXT NOT NULL
        )
        ''')
    connection.commit()
    connection.close()


# user_db()
# support_db()
# admin_db()
# superadmin_db()

def create_table_question():
    connection = sqlite3.connect('databases/question.db')
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Questions (
        id INTEGER PRIMARY KEY,
        user_id INTEGER NOT NULL,
        msg_id INTEGER NOT NULL,
        text_question TEXT NOT NULL
        )
        ''')


# create_table_question()

def create_table_active_sup():
    connection = sqlite3.connect('databases/question.db')
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS active_supports (
        id INTEGER PRIMARY KEY,
        user_id INTEGER NOT NULL
        )
        ''')

# create_table_active_sup()

def create_table_answers():
    connection = sqlite3.connect('databases/answers.db')
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS answers (
        id INTEGER PRIMARY KEY,
        user_id INTEGER NOT NULL,
        msg_id INTEGER NOT NULL,
        text_question TEXT NOT NULL,
        text_answer TEXT NOT NULL
        )
        ''')

create_table_answers()

