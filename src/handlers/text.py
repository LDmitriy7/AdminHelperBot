from aiogram import types
from aiogram.dispatcher import FSMContext

from assets import states
from core import Handler, events
from lib import parse_channels

event = events.Text()


async def callback(msg: types.Message, state: FSMContext):
    channels = parse_channels(msg)

    if not channels:
        return

    await state.update_data(channels=channels)
    await states.AddingSale.date.set()
    await msg.answer('Отправь дату (только число)')


TEXT = Handler(event, callback)
