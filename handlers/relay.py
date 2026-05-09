from aiogram import Router
from aiogram.types import Message

from services.queue import active_chats

router = Router()


@router.message()
async def relay_messages(message: Message):

    user_id = message.from_user.id

    # ignore commands/buttons
    blocked = [
        "🔍 Find Match",
        "🎭 Profile",
        "🎁 Credits"
    ]

    if message.text in blocked:
        return

    if user_id not in active_chats:
        return

    partner_id = active_chats[user_id]

    try:

        if message.text:
            await message.bot.send_message(
                partner_id,
                f"💬 {message.text}"
            )

        elif message.photo:
            await message.bot.send_photo(
                partner_id,
                photo=message.photo[-1].file_id,
                caption=message.caption or ""
            )

        elif message.voice:
            await message.bot.send_voice(
                partner_id,
                voice=message.voice.file_id
            )

    except:
        await message.answer("⚠️ Failed to send message.")
