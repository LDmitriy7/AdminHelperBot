from .database import Database
from .dispatcher import Dispatcher


class App:
    def __init__(self):
        db = Database()
        self._dp = Dispatcher(db)

    def run(self):
        from handlers import HANDLERS
        from middlewares import MIDDLEWARES

        self._dp.start_polling(HANDLERS, MIDDLEWARES)


app = App()
