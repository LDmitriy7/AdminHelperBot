from aiogram import Bot
from aiogram.types import BotCommand

START = 'start'

USER_COMMANDS = [
    BotCommand(START, 'Главное меню'),
]


async def setup():
    bot = Bot.get_current()
    await bot.set_my_commands(USER_COMMANDS)
