from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from database.db import add_user, init_db
from keyboards.main_menu import main_menu

router = Router()


@router.message(CommandStart())
async def start_cmd(message: Message):

    await init_db()
    await add_user(message.from_user.id)

    text = """
👋 <b>Welcome to VEIL</b>

No followers.
No fake flex.
Just real anonymous conversations.

Press below when you're ready 👀
"""

    await message.answer(
        text,
        reply_markup=main_menu
    )
