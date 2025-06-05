import logging
from aiogram.filters import Command
from aiogram import F
from aiogram import Router
from aiogram import types

from bot.filters.supports import IsSupport
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from loader import db_question, db_answer
from bot.keyboards.supports import sup_panel

router = Router()


class Actions(StatesGroup):
    usual = State()
    work = State()
    answer_question = State()


@router.message(Command('supportpanel'), IsSupport())
async def support_panel(msg: types.Message, state: FSMContext):
    try:
        text = "👩‍💻Привет саппорт, добро пожаловать в саппорт панель"

        await msg.answer(text, reply_markup=sup_panel())
        await state.set_state(Actions.usual)

    except Exception as err:
        # Log any errors that occur during execution
        logging.error(err)


@router.message(Command('startwork'), Actions.usual, IsSupport())
async def start_work(msg: types.Message, state: FSMContext):
    await state.set_state(Actions.work)
    with db_question as connection:
        cursor = connection.cursor()
        cursor.execute('INSERT Into active_supports (user_id) Values (?)',
                       (msg.from_user.id,))
        connection.commit()


@router.message(Command('stopwork'), Actions.work, IsSupport())
async def stop_work(msg: types.Message, state: FSMContext):
    await state.set_state(Actions.usual)
    with db_question as connection:
        cursor = connection.cursor()
        cursor.execute('Delete From active_supports Where user_id = ?',
                       (msg.from_user.id,))
        connection.commit()


@router.message(F.text == 'Следующий вопрос', Actions.work, IsSupport())
async def nex_question(msg: types.Message, state: FSMContext):
    with db_question as connection:
        cursor = connection.cursor()
        question = cursor.execute('Select * From Questions').fetchone()
        if not question:
            await msg.answer('Вопросов больше нет')
        else:
            await msg.answer(question[3])
            await state.set_data({'question': question})
            cursor.execute('Delete From Questions Where user_id = ? And msg_id = ?', (question[1], question[2]))
            connection.commit()
            await state.set_state(Actions.answer_question)


@router.message(Actions.answer_question, IsSupport())
async def answer_question(msg: types.Message, state: FSMContext):
    question = await state.get_data()
    question = question['question']
    answer = msg.text
    with db_answer as connection:
        cursor = connection.cursor()
        cursor.execute('Insert Into answers (user_id, msg_id, text_question, text_answer) Values (?, ?, ?, ?)',
                       (question[1], question[2], question[3], answer,))
        connection.commit()
    await state.set_state(Actions.work)


@router.message(Command('stateusual'), IsSupport())
async def steteusual(msg: types.Message, state: FSMContext):
    await state.set_state(Actions.usual)
