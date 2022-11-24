from aiogram import types
from aiogram.dispatcher import FSMContext

from assets import texts, commands


async def start(msg: types.Message, state: FSMContext):
    await state.finish()
    await msg.answer(texts.welcome)
    await commands.setup()
