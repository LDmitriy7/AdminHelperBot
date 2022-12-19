from datetime import datetime

import config
import models
from core import markup


def repr_time_item(value: int) -> str:
    return str(value).rjust(2, '0')


def repr_time(date_time: datetime) -> str:
    return f'{repr_time_item(date_time.hour)}:{repr_time_item(date_time.minute)}'


def repr_date(date_time: datetime) -> str:
    month = {
        1: 'января',
        2: 'февраля',
        3: 'марта',
        4: 'апреля',
        5: 'мая',
        6: 'июня',
        7: 'июля',
        8: 'августа',
        9: 'сентября',
        10: 'октября',
        11: 'ноября',
        12: 'декабря',
    }[date_time.month]

    return f'#{date_time.day}_{month}'


def repr_date_time(date_time: datetime) -> str:
    return f'📆 {repr_date(date_time)}, {repr_time(date_time)}'


def repr_channel(channel: str) -> str:
    for c in config.CHANNELS:
        if c.name == channel:
            url = c.url
            break
    else:
        url = ''

    return f'🔸 {markup.link(url, channel)}'


def repr_sale(sale: models.Sale) -> str:
    header = f'{markup.bold("Продажа")} (👤 {sale.user})'
    date_time = repr_date_time(sale.datetime)
    channels = '\n'.join(repr_channel(c) for c in sale.channels)
    return '\n\n'.join([header, date_time, channels])
