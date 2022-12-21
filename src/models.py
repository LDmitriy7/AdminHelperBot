from datetime import datetime

from mongoengine import Document, IntField, StringField, DateTimeField, ListField, ReferenceField


class Channel(Document):
    chat_id: int = IntField(primary_key=True)
    title: str = StringField()
    url: str = StringField()


class Seller(Document):
    user_id: int = IntField(primary_key=True)
    name: str = StringField()


class Post(Document):
    publish_date: datetime = DateTimeField()


class Sale(Document):
    seller: Seller = ReferenceField(Seller)
    channels: list[Channel] = ListField(ReferenceField(Channel))
    posts: list[Post] = ListField(ReferenceField(Post))
