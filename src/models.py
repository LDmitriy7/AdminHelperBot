from dataclasses import dataclass

import mongoengine as me


@dataclass
class Channel:
    name: str
    url: str


class Sale(me.Document):
    user = me.StringField()
    datetime = me.DateTimeField()
    channels = me.ListField(me.StringField())
