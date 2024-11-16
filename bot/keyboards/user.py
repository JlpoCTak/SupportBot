from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def get_main_kb() -> InlineKeyboardMarkup:
    """
    Клавиатура для главного меню (тест)
    """
    ikb = InlineKeyboardMarkup(inline_keyboard=[
       [InlineKeyboardButton(text='Кнопка 1', callback_data='cb_btn_1_main')]
    ])

    return ikb