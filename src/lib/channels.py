from aiogram import types

import config


def parse_channels(msg: types.Message) -> list[str]:
    channels = set()

    for entity in msg.entities:
        match entity.type:
            case 'mention':
                mention: str = msg.text[entity.offset:entity.offset + entity.length]
                url = mention.replace('@', 'https://t.me/')
            case 'url':
                url: str = msg.text[entity.offset:entity.offset + entity.length]
            case 'text_link':
                url = entity.url
            case _:
                continue

        for c in config.CHANNELS:
            if c.url == url:
                channels.add(c.title)

    return list(channels)
