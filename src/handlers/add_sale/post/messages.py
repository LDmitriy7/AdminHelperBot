import asyncio

from aiogram import types
from aiogram.dispatcher import FSMContext

import config
from assets import states
from core import Handler, events, lock, userbot

event = events.Message(state=states.AddingSale.post)


async def callback(msg: types.Message, state: FSMContext):
    async with lock:
        storage = await state.get_data()
        message_ids = storage.get('message_ids', [])

        if message_ids:
            await state.update_data(message_ids=message_ids + [msg.message_id])
            return

        await state.update_data(message_ids=[msg.message_id])

    await msg.answer('Загружаю посты в отлогу...')
    await asyncio.sleep(5)
    storage = await state.get_data()
    await state.finish()

    message_ids = storage['message_ids']
    channels = storage['channels']

    for c_name in channels:
        for c in config.CHANNELS:
            if c.title == c_name:
                await userbot.forward_messages(
                    c.id,
                    msg.chat.id,
                    message_ids,
                    schedule_date=storage['datetime'],
                    drop_author=True,
                )
                break

    await msg.answer('Готово!')


MESSAGES = Handler(event, callback)
