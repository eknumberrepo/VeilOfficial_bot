from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🔍 Find Match")],
        [KeyboardButton(text="🎭 Profile"),
         KeyboardButton(text="🎁 Credits")]
    ],
    resize_keyboard=True
)
