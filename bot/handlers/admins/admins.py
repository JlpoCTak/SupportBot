import logging
from loader import db
from aiogram.filters import Command
from aiogram import F
from aiogram import Router
from aiogram import types
from bot.keyboards.admins import admin_panel
from bot.filters.admin import IsAdmin
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

router = Router()


class Actions(StatesGroup):
    usual = State()
    add_sup = State()
    del_sup = State()


@router.message(Command('adminpanel'), IsAdmin())
async def main_panel(msg: types.Message, state: FSMContext):
    try:
        cid = msg.from_user.id  # The ID of the admin who initiated the action
        mid = msg.message_id  # The ID of the message to be updated
        chatid = msg.chat.id
        # Translate the greeting message
        text = "👩‍💻Привет админ, добро пожаловать в админ панель"

        # Edit the message with the translated text and update it with the main admin panel buttons
        await msg.answer(text, reply_markup=admin_panel())

    except Exception as err:
        # Log any errors that occur during execution
        logging.error(err)


@router.message(F.text == 'Добавить саппорта', IsAdmin())
async def tell_username_add_sup(msg: types.Message, state: FSMContext):
    await state.set_state(Actions.add_sup)
    await msg.answer('Введите username пользователя которого хотите добавить с знаком \'@\'')


@router.message(F.text == 'Удалить саппорта', IsAdmin())
async def tell_username_del_support(msg: types.Message, state: FSMContext):
    await state.set_state(Actions.del_sup)
    await msg.answer('Введите username пользователя которого хотите удалить с знаком \'@\'')


@router.message(F.text.startswith('@'), IsAdmin(), Actions.add_sup)
async def add_support(msg: types.Message, state: FSMContext):
    username_to_add = msg.text[1:]
    with db as connection:
        cursor = connection.cursor()
        data_user = cursor.execute('Select * From Users Where telegram_user_username = ?',
                                   (username_to_add,)).fetchall()
        if data_user == []:
            await msg.answer('Данного пользователя нет в нашей базе данных.\n'
                             'Проверьте верность вводимых данных или попросите пользователя перейти в данного бота и нажать кнопку \"Начать\"')
            await msg.answer_photo(photo=types.FSInputFile('databases/img/qr.png'))
        else:
            data_user = [x for x in data_user[0]]
            cursor.execute(
                'Insert Into Supports (telegram_user_fullname, telegram_user_username, telegram_user_id)'
                ' Values (?, ?, ?)',
                (data_user[1], data_user[2], data_user[3],))
            await msg.answer('Оператор службы поддержки успешно добавлен')
            connection.commit()

    await state.set_state(Actions.usual)


@router.message(F.text.startswith('@'), IsAdmin(), Actions.del_sup)
async def add_support(msg: types.Message, state: FSMContext):
    username_to_del = msg.text[1:]
    with db as connection:
        cursor = connection.cursor()
        data_user = cursor.execute('Select * From Supports Where telegram_user_username = ?',
                                   (username_to_del,)).fetchall()
        if data_user == []:
            await msg.answer('Данного пользователя нет в нашей базе данных.\n'
                             'Проверьте верность вводимых данных')
        else:
            data_user = [x for x in data_user[0]]
            cursor.execute(
                'Delete From Supports Where telegram_user_username = ?',
                (username_to_del,))
            await msg.answer('Оператор службы поддержки успешно удалён')
            connection.commit()

    await state.set_state(Actions.usual)
