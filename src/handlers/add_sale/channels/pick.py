from aiogram import types
from aiogram.dispatcher import FSMContext

import config
from assets import kbs, states
from core import Handler, events

event = events.Click(kbs.Channels.item, state=states.AddingSale.channels)


async def callback(query: types.CallbackQuery, button: dict, state: FSMContext):
    channel = button['channel']
    storage = await state.get_data()
    channels = storage.get('channels', [])

    if channel in channels:
        channels.remove(channel)
    else:
        channels.append(channel)

    await state.update_data(channels=channels)

    kb = kbs.Channels(config.CHANNELS, selected=channels).adapt()
    await query.message.edit_reply_markup(kb)


PICK = Handler(event, callback)
