import asyncio
import os

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message

TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID"))

bot = Bot(TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "👋 Привет!\n\n"
        "Отправь мне свой анонимный вопрос."
    )

@dp.message()
async def send_question(message: Message):
    await bot.send_message(
        ADMIN_ID,
        f"📩 Новый анонимный вопрос:\n\n{message.text}"
    )
    await message.answer("✅ Вопрос отправлен!")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
