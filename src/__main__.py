from handlers import HANDLERS
from loader import app
from middlewares import MIDDLEWARES

app.run(HANDLERS, MIDDLEWARES)
