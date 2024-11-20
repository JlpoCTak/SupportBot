import logging
from aiogram.utils.keyboard import ReplyKeyboardMarkup, KeyboardButton


def admin_panel():
    button_add_support = KeyboardButton(text='Добавить саппорта')
    button_del_support = KeyboardButton(text='Удалить саппорта')
    admin_pan = ReplyKeyboardMarkup(keyboard=[
        [button_add_support],
        [button_del_support]],
        resize_keyboard=True
    )
    return admin_pan
