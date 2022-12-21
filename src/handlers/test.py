from aiogram import types
from aiogram.dispatcher import FSMContext

from assets import commands
from core import Handler, events, userbot

event = events.Command(commands.TEST, state='*')


async def callback(msg: types.Message, state: FSMContext):
    await userbot.start()
    await userbot.send_message('@test7244bot', '...')


TEST = Handler(event, callback)
