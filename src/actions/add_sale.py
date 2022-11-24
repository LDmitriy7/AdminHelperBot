from aiogram import types
from aiogram.dispatcher import FSMContext

from assets import states


async def ask_channels(msg: types.Message):
    await states.AddingSale.channels.set()
    await msg.answer('Каналы?')


async def ask_date(msg: types.Message):
    await states.AddingSale.date.set()
    await msg.answer('Дата?')


async def ask_time(msg: types.Message):
    await states.AddingSale.time.set()
    await msg.answer('Время?')


async def finish(msg: types.Message, state: FSMContext):
    await state.finish()
    await msg.answer('Готово')
