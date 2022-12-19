from aiogram import types
from aiogram.dispatcher import FSMContext

import config
from assets import commands, states
from core import Handler, events, userbot

event = events.Command(commands.USERBOT, user_id=config.OWNER_ID)


async def callback(msg: types.Message, state: FSMContext):
    is_authorized = await userbot.connect()

    if is_authorized:
        await msg.answer('Юзербот уже авторизован')
        return

    await states.UserbotAuth.phone_code.set()

    sent_code = await userbot.send_code(userbot.phone_number)
    await state.update_data(phone_code_hash=sent_code.phone_code_hash)
    await msg.answer('Отправь код авторизации')


START = Handler(event, callback)
