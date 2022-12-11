from aiogram import types
from aiogram.dispatcher import FSMContext

from assets import states, kbs
from core import Handler, events

event = events.Click(kbs.Skip.button, state=states.AddingSale.post)


async def callback(query: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await query.message.delete()


SKIP = Handler(event, callback)
