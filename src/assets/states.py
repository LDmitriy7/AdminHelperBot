from aiogram.dispatcher.filters.state import StatesGroup, State


class AddingSale(StatesGroup):
    channels = State()
    date = State()
    time = State()
    post = State()


class UserbotAuth(StatesGroup):
    phone_code = State()
