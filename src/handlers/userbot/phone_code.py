from aiogram import types
from aiogram.dispatcher import FSMContext

from assets import states
from core import Handler, events, userbot

event = events.Text(state=states.UserbotAuth.phone_code)


async def callback(msg: types.Message, state: FSMContext):
    userbot.phone_code = msg.text
    await state.finish()
    await userbot.start()

    if userbot.is_initialized:
        await msg.answer('Юзербот успешно авторизован')


PHONE_CODE = Handler(event, callback)
