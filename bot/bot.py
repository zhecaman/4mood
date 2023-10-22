import asyncio
import logging
from aiogram import Bot, Dispatcher,types

from aiogram.filters.command import Command


bot = Bot(token='')
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer(f"Hello, {message.chat.id}")

@dp.message(Command('dkny'))
async def dkny(message:types.Message):
    file = open('sale.csv', 'rb')
    await bot.send_document(chat_id=message.chat.id, document=file)


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
