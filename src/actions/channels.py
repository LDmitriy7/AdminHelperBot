from aiogram import types

import config


async def show_channels(msg: types.Message):
    channels = [f'🔸 <a href="{c.url}">{c.name}</a>' for c in config.CHANNELS]
    text = '\n\n'.join(channels)
    await msg.answer(text)
