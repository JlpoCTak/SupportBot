
from aiogram.filters import BaseFilter
from aiogram.types import Message
from data.config import ADMIN
from loader import db


class IsSupport(BaseFilter):
    """
    Filter to check if the user is a support or the super admin.

    Attributes:
        ADMIN (int): The ID of the super admin.
    """

    def __init__(self):
        self.ADMIN = ADMIN

    async def __call__(self, message: Message) -> bool:
        """
        Checks if the message sender is a support or the super admin.

        Args:
            message (Message): The message object from the user.

        Returns:
            bool: True if the user is a support or the super admin, False otherwise.
        """

        with db as connection:
            cursor = connection.cursor()
            supports = cursor.execute('Select telegram_user_id From Supports')
            supports_k = []
            for _ in supports:
                supports_k.append(int(_[0]))
        self.cid = message.from_user.id
        if self.cid == ADMIN:
            return True
        elif self.cid in supports_k:
            return True
        else:
            return False

