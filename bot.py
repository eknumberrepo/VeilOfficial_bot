from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
import asyncio

from config import BOT_TOKEN
from handlers.start import router as start_router
from handlers.matchmaking import router as match_router
from handlers.relay import router as relay_router

bot = Bot(
    token=BOT_TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)

dp = Dispatcher()

dp.include_router(start_router)
dp.include_router(match_router)
dp.include_router(relay_router)


async def main():
    print("✅ VEIL Bot Started")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
