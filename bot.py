import asyncio
import os
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import CommandStart

TOKEN = os.getenv("8773515752:AAGIXz1t-JhRIbPMV46pfvnyQAl_G8c6u-Q")

if not TOKEN:
    raise ValueError("8773515752:AAGIXz1t-JhRIbPMV46pfvnyQAl_G8c6u-Q не найден в переменных окружения")

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer("Бот работает.")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
