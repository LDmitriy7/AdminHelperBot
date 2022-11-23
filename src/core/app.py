from aiogram.dispatcher.middlewares import BaseMiddleware

from .database import Database
from .dispatcher import Dispatcher
from .handler_group import HandlerGroup


class App:
    def __init__(self, bot_token: str, db: Database):
        self._dp = Dispatcher(bot_token, db)

    def run(self, handlers: HandlerGroup, middlewares: list[BaseMiddleware]):
        self._dp.start_polling(handlers, middlewares)
