from aiogram.types import BotCommand

import config
from lib import set_chats_commands

START = 'start'
ADD_SALE = 'add_sale'
CHANNELS = 'channels'
TEST = 'test'

ADMIN_COMMANDS = [
    BotCommand(ADD_SALE, 'Добавить продажу'),
    BotCommand(CHANNELS, 'Список каналов'),
    BotCommand(START, 'Перезапустить бота'),
]


async def setup():
    await set_chats_commands(ADMIN_COMMANDS, config.REPORT_GROUP_ID, no_error=True)
