import asyncio

import structlog
from aiogram import Bot, Dispatcher
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.filters import Command

from exceptions import WeatherAPIException
from redis_helper import set_user_language, get_user_language
from utils import set_commands, send_language_selection
from variables import *
from weather_client import WeatherClient

logger = structlog.get_logger(__name__)

bot = Bot(TELEGRAM_BOT_TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def start_command(message: Message):
    await message.answer("Привет!")
    await send_language_selection(message)


@dp.message(Command("change_language"))
async def change_language(message: Message):
    await send_language_selection(message)


@dp.message(lambda message: message.text in ['Русский', 'English'])
async def language_selection(message: Message):
    if message.text == 'Русский':
        await set_user_language(message.from_user.id, 'ru')
        await message.answer(
            "Вы выбрали русский язык. Введите название города:",
            reply_markup=ReplyKeyboardRemove()
        )
    elif message.text == 'English':
        await set_user_language(message.from_user.id, 'en')
        await message.answer(
            "You selected English. Please enter the name of the city:",
            reply_markup=ReplyKeyboardRemove()
        )


@dp.message()
async def send_weather(message: Message):
    logger.info('Message recieved.', message=message)
    city = message.text
    lang = await get_user_language(message.from_user.id)  # russian by default

    try:
        weather = await WeatherClient.get_weather(city, lang)
    except WeatherAPIException as e:
        await message.answer(str(e))
        return

    if lang == 'ru':
        response_message = (
            f"Погода в городе {city}:\n"
            f"Температура: {weather['temperature']}°C\n"
            f"Влажность: {weather['humidity']}%\n"
            f"Описание: {weather['description']}"
        )
    else:
        response_message = (
            f"Weather in {city}:\n"
            f"Temperature: {weather['temperature']}°C\n"
            f"Humidity: {weather['humidity']}%\n"
            f"Description: {weather['description']}"
        )
    await message.answer(response_message)


async def main():
    await set_commands(bot)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logger.info('Bot started.')
    asyncio.run(main())
