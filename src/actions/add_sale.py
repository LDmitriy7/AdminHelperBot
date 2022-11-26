from aiogram import types
from aiogram.dispatcher import FSMContext

import config
from assets import kbs
from assets import states


async def ask_channels(msg: types.Message):
    await states.AddingSale.channels.set()
    kb = kbs.Channels(config.CHANNELS, selected=[]).adapt()
    await msg.answer('Отметь каналы:', reply_markup=kb)


async def pick_channel(query: types.CallbackQuery, button: dict, state: FSMContext):
    name = button['name']
    storage = await state.get_data()
    channels = storage.get('channels', [])

    if name in channels:
        channels.remove(name)
    else:
        channels.append(name)

    await state.update_data(channels=channels)

    kb = kbs.Channels(config.CHANNELS, selected=channels).adapt()
    await query.message.edit_reply_markup(kb)


async def pick_all_channels(query: types.CallbackQuery, state: FSMContext):
    channels = [c.name for c in config.CHANNELS]
    await state.update_data(channels=channels)

    kb = kbs.Channels(config.CHANNELS, selected=channels).adapt()
    await query.message.edit_reply_markup(kb)


async def ask_date(query: types.CallbackQuery):
    await states.AddingSale.date.set()
    await query.message.answer('Дата?')


async def ask_time(msg: types.Message):
    await states.AddingSale.time.set()
    await msg.answer('Время?')


async def finish(msg: types.Message, state: FSMContext):
    await state.finish()
    await msg.answer('Готово')
