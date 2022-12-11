from aiogram import types
from aiogram.dispatcher import FSMContext

from assets import commands
from core import Handler, events

event = events.Command(commands.TEST, state='*')


async def callback(msg: types.Message, state: FSMContext):
    pass


TEST = Handler(event, callback)
