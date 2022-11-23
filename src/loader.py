import config
from core import App, Database

db = Database(config.MONGO_DB, config.MONGO_HOST, config.MONGO_USER, config.MONGO_PASSWORD)
app = App(config.BOT_TOKEN, db)
