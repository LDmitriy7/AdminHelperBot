from aiogram import types
from aiogram.dispatcher import FSMContext

import config
from assets import kbs, commands, states
from core import Handler, events

event = events.Command(commands.ADD_SALE, user_id=config.ADMINS_IDS, state='*')


async def callback(msg: types.Message, state: FSMContext):
    await state.finish()
    await states.AddingSale.channels.set()
    kb = kbs.Channels(config.CHANNELS, selected=[]).adapt()
    await msg.answer('Отметь каналы:', reply_markup=kb)


START = Handler(event, callback)
