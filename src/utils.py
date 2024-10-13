from aiogram import Bot
from aiogram.types import (
    Message,
    ReplyKeyboardMarkup,
    KeyboardButton,
    BotCommand
)


async def send_language_selection(message: Message):
    language_keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text='Русский')],
            [KeyboardButton(text='English')]
        ],
        resize_keyboard=True
    )
    await message.answer("Выбери язык / Choose a language:", reply_markup=language_keyboard)


async def set_commands(bot: Bot):
    commands = [
        BotCommand(command="/start", description="Запустить бота"),
        BotCommand(command="/change_language", description="Изменить язык")
    ]
    await bot.set_my_commands(commands)
