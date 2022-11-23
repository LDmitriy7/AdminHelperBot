from core import env

BOT_TOKEN = env.get('BOT_TOKEN')
MONGO_DB = 'AdminHelperBot'
MONGO_HOST = env.get('MONGO_HOST')
MONGO_USER = env.get('MONGO_USER', None)
MONGO_PASSWORD = env.get('MONGO_PASSWORD', None)
