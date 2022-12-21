from core import env
from models import Channel

ADMINS_IDS = [724477101, 936845322, 677293584, 5253920596, 2062674929, 1149906530]
OWNER_ID = 724477101  # 1980530667
REPORT_GROUP_ID = env.get_int('REPORT_GROUP_ID')

_channels_data = [
    (-1001300460444, 'Акиет', 'https://t.me/akiet'),
    (-1001583208278, 'Аниме новинки', 'https://t.me/animeipikchi'),
    (-1001738529532, 'Баблкам', 'https://t.me/bubblekum'),
    (-1001446620325, 'Диундер', 'https://t.me/diunder'),
    (-1001592432164, 'Крутые авы', 'https://t.me/anime4_avatarki'),
    (-1001271558289, 'Мультач', 'https://t.me/multtach'),
    (-1001298167864, 'Парные', 'https://t.me/avy_parnye_avatarki'),
    (-1001563981037, 'Пикзери', 'https://t.me/pikzery'),
    (-1001554954940, 'Пикчи для диалогов', 'https://t.me/kartinki_avatarki'),
    (-1001573250306, 'Стикеры', 'https://t.me/anime4_arts'),
    (-1001191474106, 'Тянки', 'https://t.me/anime4_tyan'),
    (-1001611457973, 'Юри', 'https://t.me/ero_anime_tyan'),
    (-1001582829502, 'Zxc', 'https://t.me/pikchidlygylei000'),
]

CHANNELS = [Channel(chat_id=i[0], title=i[1], url=i[2]).save() for i in _channels_data]
