from aiogram import types
from aiogram.dispatcher import FSMContext

import config
import models
from assets import states
from core import Handler, events, bot
from lib import resolve_datetime, repr_sale

event = events.Text(state=states.AddingSale.time)


async def callback(msg: types.Message, state: FSMContext):
    storage = await state.get_data()
    try:
        datetime = resolve_datetime(msg.text, storage['datetime'])
    except ValueError:
        await msg.answer('Ошибка, отправь время в верном формате')
        return

    sale = models.Sale(
        user=msg.from_user.full_name,
        datetime=datetime,
        channels=storage['channels'],
    ).save()

    await state.finish()
    text = repr_sale(sale)
    report_msg = await bot.send_message(config.REPORT_GROUP_ID, text)
    await msg.answer(f'Готово: {report_msg.url}')


TIME = Handler(event, callback)
