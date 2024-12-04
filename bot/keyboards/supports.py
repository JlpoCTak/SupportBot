from aiogram.utils.keyboard import ReplyKeyboardMarkup, KeyboardButton


def sup_panel():
    button_add_support = KeyboardButton(text='/startwork')
    button_next_quest = KeyboardButton(text='Следующий вопрос')
    button_del_support = KeyboardButton(text='/stopwork')
    sup_pan = ReplyKeyboardMarkup(keyboard=[
        [button_add_support],
        [button_next_quest],
        [button_del_support]],
        resize_keyboard=True
    )
    return sup_pan
