
from aiogram.filters import BaseFilter
from aiogram.types import Message
from data.config import ADMIN
from loader import db


class IsSupport(BaseFilter):
    """
    Filter to check if the user is support.

    Attributes:
        support (int): The ID of the super admin.
    """

    def __init__(self, support):
        self.SUPPORT = support

    async def __call__(self, message: Message) -> bool:
        """
        Checks if the message sender is a support.

        Args:
            message (Message): The message object from the user.

        Returns:
            bool: True if the user is a support, False otherwise.
        """
        with db as connection:
            cursor = connection.cursor()
            supports = cursor.execute('Select telegram_user_id From Supports')
            SUPPORTS = []
            for _ in supports:
                SUPPORTS.append(int(_[0]))
            print(SUPPORTS)
        self.cid = message.from_user.id
        if self.cid in SUPPORTS:
            print('да сапорт')
            return True
        else:
            print('не сап')
            return False

