from aiogram import types
from aiogram.dispatcher import FSMContext

from assets import states
from core import Handler, events, userbot

event = events.Text(state=states.UserbotAuth.phone_code)


async def callback(msg: types.Message, state: FSMContext):
    storage = await state.get_data()
    phone_code_hash = storage['phone_code_hash']
    phone_code = msg.text
    print(phone_code_hash)
    print(phone_code)
    userbot.authorize()

    signed_in = await userbot.sign_in(userbot.phone_number, phone_code_hash, phone_code)
    print(signed_in)

    await state.finish()
    await msg.answer('Юзербот успешно авторизован')


PHONE_CODE = Handler(event, callback)
