from aiogram import types

from assets import commands
from core import Handler, events

event = events.Command(commands.TEST, state='*')


async def callback(msg: types.Message):
    await msg.answer('test')


TEST = Handler(event, callback)
