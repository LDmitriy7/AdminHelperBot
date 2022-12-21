from aiogram import types

import config
from assets import commands, states
from core import Handler, events, userbot

event = events.Command(commands.USERBOT, user_id=config.OWNER_ID)


async def callback(msg: types.Message):
    if userbot.is_initialized:
        await msg.answer('Юзербот уже инициализирован')
        return

    is_authorized = await userbot.connect()

    if is_authorized:
        await userbot.start()
        await msg.answer('Юзербот инициализирован')
        return

    userbot.sent_code = await userbot.send_code(userbot.phone_number)
    await states.UserbotAuth.phone_code.set()
    await msg.answer('Отправь код авторизации')


START = Handler(event, callback)
