from aiogram import types
from aiogram.dispatcher import FSMContext

import config
from assets import kbs, states
from core import Handler, events

event = events.Click(kbs.Channels.pick_all, state=states.AddingSale.channels)


async def callback(query: types.CallbackQuery, state: FSMContext):
    channels = [c.name for c in config.CHANNELS]
    await state.update_data(channels=channels)

    kb = kbs.Channels(config.CHANNELS, selected=channels).adapt()
    await query.message.edit_reply_markup(kb)


PICK_ALL = Handler(event, callback)
