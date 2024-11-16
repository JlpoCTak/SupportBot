import asyncio
import logging
import sys
import os

from loader import *

import bot.handlers.users.users as users


async def main() -> None:
    """
    Главная функция запускающая бота
    """
    dp.include_routers(users.router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
