from aiogram import types

import config
from assets import commands
from core import Handler, events, markup

event = events.Command(commands.CHANNELS, state='*')


async def callback(msg: types.Message):
    strings = [f'🔸 {markup.link(c.url, c.name)}' for c in config.CHANNELS]
    text = '\n\n'.join(strings)
    await msg.answer(text)


CHANNELS = Handler(event, callback)
