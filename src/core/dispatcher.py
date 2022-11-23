import aiogram
from aiogram.contrib.fsm_storage.mongo import MongoStorage
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.utils import executor

from .database import Database
from .handler import Handler
from .handler_group import HandlerGroup


class Dispatcher:
    def __init__(self, bot_token: str, db: Database):
        self._bot_token = bot_token
        self._db = db

    def _create_raw(self) -> aiogram.Dispatcher:
        from . import middlewares

        bot = aiogram.Bot(self._bot_token, parse_mode='html', disable_web_page_preview=True)
        storage = MongoStorage(
            host=self._db.host,
            db_name=self._db.name,
            username=self._db.user,
            password=self._db.password,
        )
        dp = aiogram.Dispatcher(bot, storage=storage)
        dp.setup_middleware(middlewares.AnswerAnyQuery())
        return dp

    def start_polling(self, handlers: HandlerGroup, middlewares: list[BaseMiddleware]):
        dp = self._create_raw()
        self._setup_handlers(handlers, dp)
        self._setup_middlewares(middlewares, dp)
        executor.start_polling(dp)

    def _setup_handlers(self, handlers: HandlerGroup, dp: aiogram.Dispatcher):
        for handler in handlers:
            self._setup_handler(handler, dp)

    def _setup_middlewares(self, middlewares: list[BaseMiddleware], dp: aiogram.Dispatcher):
        for m in middlewares:
            self._setup_middleware(m, dp)

    @staticmethod
    def _setup_handler(handler: Handler, dp: aiogram.Dispatcher):
        decorator = handler.event.as_decorator(dp)
        decorator(handler.callback)

    @staticmethod
    def _setup_middleware(middleware: BaseMiddleware, dp: aiogram.Dispatcher):
        dp.setup_middleware(middleware)
