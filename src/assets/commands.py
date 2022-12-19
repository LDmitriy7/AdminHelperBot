from aiogram.types import BotCommand

import config
from lib import set_chats_commands

START = 'start'
ADD_SALE = 'add_sale'
CHANNELS = 'channels'
TEST = 'test'
USERBOT = 'userbot'

ADMIN_COMMANDS = [
    BotCommand(ADD_SALE, 'Добавить продажу'),
    BotCommand(CHANNELS, 'Список каналов'),
    BotCommand(START, 'Перезапустить бота'),
]

OWNER_COMMANDS = ADMIN_COMMANDS + [
    BotCommand(USERBOT, 'Управление юзерботом'),
]


async def setup():
    await set_chats_commands(ADMIN_COMMANDS, [config.REPORT_GROUP_ID], no_error=True)
    await set_chats_commands(OWNER_COMMANDS, [config.OWNER_ID])
