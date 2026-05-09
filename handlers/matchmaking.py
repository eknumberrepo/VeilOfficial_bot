from aiogram import Router
from aiogram.types import Message

from services.queue import waiting_users, active_chats

router = Router()


@router.message(lambda msg: msg.text == "🔍 Find Match")
async def find_match(message: Message):

    user_id = message.from_user.id

    # already chatting
    if user_id in active_chats:
        await message.answer("⚠️ You're already in a chat.")
        return

    # already waiting
    if user_id in waiting_users:
        await message.answer("⏳ Searching for someone...")
        return

    # match found
    if waiting_users:

        partner = waiting_users.pop(0)

        active_chats[user_id] = partner
        active_chats[partner] = user_id

        await message.answer("🎉 Match found! Say hi 👀")
        await message.bot.send_message(
            partner,
            "🎉 Match found! Say hi 👀"
        )

    else:
        waiting_users.append(user_id)
        await message.answer("🔎 Looking for someone online...")
