from core import env
from models import Channel

ADMINS_IDS = [724477101, 936845322, 677293584, 5253920596, 2062674929, 1149906530]
OWNER_ID = 724477101
REPORT_GROUP_ID = env.get_int('REPORT_GROUP_ID')

CHANNELS = [
    Channel(-1001300460444, 'Акиет', 'https://t.me/akiet'),
    Channel(-1001583208278, 'Аниме новинки', 'https://t.me/animeipikchi'),
    Channel(-1001738529532, 'Баблкам', 'https://t.me/bubblekum'),
    Channel(-1001446620325, 'Диундер', 'https://t.me/diunder'),
    Channel(-1001592432164, 'Крутые авы', 'https://t.me/anime4_avatarki'),
    Channel(-1001271558289, 'Мультач', 'https://t.me/multtach'),
    Channel(-1001298167864, 'Парные', 'https://t.me/avy_parnye_avatarki'),
    Channel(-1001563981037, 'Пикзери', 'https://t.me/pikzery'),
    Channel(-1001554954940, 'Пикчи для диалогов', 'https://t.me/kartinki_avatarki'),
    Channel(-1001573250306, 'Стикеры', 'https://t.me/anime4_arts'),
    Channel(-1001191474106, 'Тянки', 'https://t.me/anime4_tyan'),
    Channel(-1001611457973, 'Юри', 'https://t.me/ero_anime_tyan'),
    Channel(-1001582829502, 'Zxc', 'https://t.me/pikchidlygylei000'),
]
