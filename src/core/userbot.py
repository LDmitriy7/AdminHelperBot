from datetime import datetime
from typing import Iterable

import pyrogram
from pyrogram import utils, raw, types, errors

from . import config


class Userbot(pyrogram.Client):
    def __init__(self, api_id: int, api_hash: str, phone_number: str, password: str):
        self.sent_code: types.SentCode | None = None
        super().__init__(
            config.USERBOT_SESSION_PATH,
            api_id,
            api_hash,
            phone_number=phone_number,
            password=password,
        )

    async def forward_messages(
            self,
            chat_id: int | str,
            from_chat_id: int | str,
            message_ids: int | Iterable[int],
            disable_notification: bool = None,
            schedule_date: datetime = None,
            protect_content: bool = None,
            drop_author: bool = None,
    ) -> types.Message | types.List[types.Message]:

        is_iterable = not isinstance(message_ids, int)
        message_ids = list(message_ids) if is_iterable else [message_ids]

        r = await self.invoke(
            raw.functions.messages.ForwardMessages(
                to_peer=await self.resolve_peer(chat_id),
                from_peer=await self.resolve_peer(from_chat_id),
                id=message_ids,
                silent=disable_notification or None,
                random_id=[self.rnd_id() for _ in message_ids],
                schedule_date=utils.datetime_to_timestamp(schedule_date),
                noforwards=protect_content,
                drop_author=drop_author,
            )
        )

        forwarded_messages = []

        users = {i.id: i for i in r.users}
        chats = {i.id: i for i in r.chats}

        for i in r.updates:
            if isinstance(i, (raw.types.UpdateNewMessage,
                              raw.types.UpdateNewChannelMessage,
                              raw.types.UpdateNewScheduledMessage)):
                # noinspection PyProtectedMember
                forwarded_messages.append(
                    await types.Message._parse(
                        self, i.message,
                        users, chats
                    )
                )

        return types.List(forwarded_messages) if is_iterable else forwarded_messages[0]

    async def authorize(self) -> types.User:
        try:
            signed_in = await self.sign_in(self.phone_number, self.sent_code.phone_code_hash, self.phone_code)
        except errors.SessionPasswordNeeded:
            signed_in = await self.check_password(self.password)

        return signed_in

    async def connect(self) -> bool:
        try:
            is_authorized = await super().connect()
        except ConnectionError:
            is_authorized = bool(await self.storage.user_id())

        return is_authorized


userbot = Userbot(
    config.USERBOT_API_ID,
    config.USERBOT_API_HASH,
    config.PHONE_NUMBER,
    config.PASSWORD,
)
