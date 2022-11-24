from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeChat, BotCommandScope
from aiogram.utils.exceptions import TelegramAPIError


async def set_chats_commands(commands: list[BotCommand], chat_ids: list[int], no_error: bool = False):
    for chat_id in chat_ids:
        scope = BotCommandScopeChat(chat_id)
        await _set_chat_commands(commands, scope, no_error)


async def _set_chat_commands(commands: list[BotCommand], scope: BotCommandScope, no_error: bool):
    bot = Bot.get_current()

    try:
        await bot.set_my_commands(commands, scope)
    except TelegramAPIError as e:
        if not no_error:
            raise e
