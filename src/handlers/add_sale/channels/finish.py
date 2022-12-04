from aiogram import types
from aiogram.dispatcher import FSMContext

from assets import states, kbs
from core import Handler, events

event = events.Click(kbs.Channels.finish, state=states.AddingSale.channels)


async def callback(query: types.CallbackQuery, state: FSMContext):
    storage = await state.get_data()

    if not storage.get('channels', []):
        await query.answer('Выбери хотя бы один канал')
        return

    await states.AddingSale.date.set()
    await query.message.answer('Отправь дату (только число)')


FINISH = Handler(event, callback)
