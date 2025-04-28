import asyncio
import logging
import sqlite3
import sys
import os

from loader import *

import bot.handlers.admins.admins as admins
import bot.handlers.users.users as users
import bot.handlers.supports.supports as supports

from bot.functions.functions import check_unanswer_question


async def main() -> None:
    """
    Главная функция запускающая бота
    """
    dp.include_routers(admins.router, users.router, supports.router)
    task = asyncio.create_task(check_unanswer_question())
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
