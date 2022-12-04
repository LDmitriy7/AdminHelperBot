import models
from core.keyboards import CallbackButton, InlineKeyboard


class Channels(InlineKeyboard):
    item = CallbackButton('{channel_and_prefix}', 'Channels.item:{channel}')
    pick_all = CallbackButton('➕ Выбрать все', 'Channels.pick_all')
    finish = CallbackButton('✅ Готово', 'Channels.finish')

    def _make_item(self, channel: models.Channel, selected: list[str]) -> CallbackButton:
        channel = channel_and_prefix = channel.name

        if channel in selected:
            channel_and_prefix = '🔸 ' + channel

        return self.item.format(channel_and_prefix=channel_and_prefix, channel=channel)

    def __init__(self, channels: list[models.Channel], selected: list[str]):
        buttons = [self._make_item(c, selected) for c in channels]
        self.add_rows(*buttons, width=2)
        self.add_row(self.pick_all, self.finish)
