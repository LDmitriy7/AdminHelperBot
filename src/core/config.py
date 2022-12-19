from .env import env

BOT_TOKEN = env.get('BOT_TOKEN')
MONGO_DB = env.get('MONGO_DB')
MONGO_HOST = env.get('MONGO_HOST', 'localhost')
MONGO_USER = env.get('MONGO_USER', None)
MONGO_PASSWORD = env.get('MONGO_PASSWORD', None)
USERBOT_API_ID = env.get_int('USERBOT_API_ID')
USERBOT_API_HASH = env.get('USERBOT_API_HASH')
PHONE_NUMBER = env.get('USERBOT_PHONE_NUMBER')
PASSWORD = env.get('USERBOT_PASSWORD')
