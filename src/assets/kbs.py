import models
from core.keyboards import CallbackButton, InlineKeyboard


class Channels(InlineKeyboard):
    item = CallbackButton('{name_with_prefix}', 'Channels.item:{name}')
    pick_all = CallbackButton('➕ Выбрать все', 'Channels.pick_all')
    finish = CallbackButton('✅ Готово', 'Channels.finish')

    def _make_item(self, channel: models.Channel, selected: list[str]) -> CallbackButton:
        name = name_with_prefix = channel.name

        if name in selected:
            name_with_prefix = '🔸 ' + name

        return self.item.format(name_with_prefix=name_with_prefix, name=name)

    def __init__(self, channels: list[models.Channel], selected: list[str]):
        buttons = [self._make_item(c, selected) for c in channels]
        self.add_rows(*buttons, width=2)
        self.add_row(self.pick_all, self.finish)
