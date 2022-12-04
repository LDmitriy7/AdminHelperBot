from aiogram import types
from aiogram.dispatcher import FSMContext

from assets import texts, commands
from core import Handler, events

event = events.Command(commands.START, state='*')


async def callback(msg: types.Message, state: FSMContext):
    await state.finish()
    await msg.answer(texts.welcome)
    await commands.setup()


START = Handler(event, callback)
