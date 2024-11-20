import logging
from loader import db

from aiogram.filters import Command
from aiogram import F
from aiogram import Router
from aiogram import types

from bot.filters.supports import IsSupport
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

router = Router()


class Actions(StatesGroup):
    usual = State()
    work = State()


@router.message(Command('startwork'), IsSupport())
async def main_panel(msg: types.Message, state: FSMContext):
    await msg.answer('вроде все ок')
