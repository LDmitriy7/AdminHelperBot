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

    seller = models.Seller(user_id=msg.from_user.id, name=msg.from_user.full_name).save()
    channels = models.Channel.objects(title__in=storage['channels'])
    posts = [models.Post(publish_date=datetime).save()]

    sale = models.Sale(
        seller=seller,
        posts=posts,
        channels=channels,
    ).save()

    await states.AddingSale.post.set()

    text = repr_sale(sale)
    await bot.send_message(config.REPORT_GROUP_ID, text)
    kb = kbs.Skip().adapt()
    await msg.answer(texts.ask_post, reply_markup=kb)


TIME = Handler(event, callback)
