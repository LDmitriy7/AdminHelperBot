from aiogram import types

from assets import kbs


async def test(msg: types.Message):
    await msg.answer('test')
