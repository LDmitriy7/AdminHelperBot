from aiogram.types import BotCommand

import config
from lib import set_chats_commands

START = 'start'
ADD_SALE = 'add_sale'
TEST = 'test'

ADMIN_COMMANDS = [
    BotCommand(ADD_SALE, 'Добавить продажу'),
    BotCommand(START, 'Перезапустить бота'),
]


async def setup():
    await set_chats_commands(ADMIN_COMMANDS, config.ADMINS_IDS, no_error=True)
