from aiogram.dispatcher.filters.state import StatesGroup, State


class Order(StatesGroup):
    region = State()
    product = State()
    confirmation = State()
    payment = State()
