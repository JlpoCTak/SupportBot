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
