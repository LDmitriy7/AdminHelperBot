from aiogram import types
from aiogram.dispatcher import FSMContext

from assets import states
from core import Handler, events, markup
from lib import resolve_date

event = events.Text(state=states.AddingSale.date)


async def callback(msg: types.Message, state: FSMContext):
    try:
        date = resolve_date(msg.text)
    except ValueError:
        await msg.answer('Ошибка в дате, отправь верное число')
        return

    await states.AddingSale.time.set()
    await state.update_data(datetime=date)
    await msg.answer(f'Отправь время в формате: {markup.bold("19 05")}')


DATE = Handler(event, callback)
