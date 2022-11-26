from core import env
from models import Channel

BOT_TOKEN = env.get('BOT_TOKEN')
MONGO_DB = 'AdminHelperBot'
MONGO_HOST = env.get('MONGO_HOST')
MONGO_USER = env.get('MONGO_USER', None)
MONGO_PASSWORD = env.get('MONGO_PASSWORD', None)

ADMINS_IDS = [724477101, ]

CHANNELS = [
    Channel('Акиет', 'https://t.me/akiet'),
    Channel('Аниме новинки', 'https://t.me/animeipikchi'),
    Channel('Баблкам', 'https://t.me/bubblekum'),
    Channel('Диундер', 'https://t.me/diunder'),
    Channel('Крутые авы', 'https://t.me/anime4_avatarki'),
    Channel('Мультач', 'https://t.me/multtach'),
    Channel('Парные', 'https://t.me/avy_parnye_avatarki'),
    Channel('Пикзери', 'https://t.me/pikzery'),
    Channel('Пикчи для диалогов', 'https://t.me/kartinki_avatarki'),
    Channel('Стикеры', 'https://t.me/anime4_arts'),
    Channel('Тянки', 'https://t.me/anime4_tyan'),
    Channel('Юри', 'https://t.me/ero_anime_tyan'),
]
