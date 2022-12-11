from aiogram import types
from aiogram.dispatcher import FSMContext

import config
import models
from assets import states, texts, kbs
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

    await state.update_data(datetime=datetime)

    sale = models.Sale(
        user=msg.from_user.full_name,
        datetime=datetime,
        channels=storage['channels'],
    ).save()

    await states.AddingSale.post.set()

    text = repr_sale(sale)
    await bot.send_message(config.REPORT_GROUP_ID, text)
    kb = kbs.Skip().adapt()
    await msg.answer(texts.ask_post, reply_markup=kb)


TIME = Handler(event, callback)
