import asyncio  # Работа с асинхронностью

from aiogram import Bot, Dispatcher, F
from aiogram.enums import ContentType
from aiogram.filters import Command, Text  # Фильтр для /start, /...
from aiogram.types import Message  # Тип сообщения

from config import config  # Config

API_TOKEN = config.token

bot = Bot(token=API_TOKEN)
dp = Dispatcher()  # Менеджер бота


# dp.message - обработка сообщений
# Command(commands=['start'] Фильтр для сообщений, берём только /start
@dp.message(Command(commands=['start']))  # Берём только сообщения, являющиеся командой /start
async def start_command(message: Message):  # message - сообщение, которое прошло через фильтр
    await message.answer("Привет!")  # Отвечаем на полученное сообщение


async def main():
    try:
        print('Bot Started')
        await dp.start_polling(bot)
    finally:
        await bot.session.close()
@dp.message()
async def echo_all(message: Message):
    await message.send_copy(message.chat.id)
@dp.message(Text(text='Ответь'))
async def reply(message: Message):
    await message.reply('Ответил')


if __name__ == '__main__':  # Если мы запускаем конкретно этот файл.
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print('Bot stopped')
