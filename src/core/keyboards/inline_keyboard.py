from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


class CallbackButton:
    def __init__(self, text: str, data: str = None):
        self.text = text
        self.data = data or text

    def adapt(self) -> InlineKeyboardButton:
        return InlineKeyboardButton(self.text, callback_data=self.data)


class UrlButton:
    def __init__(self, text: str, url: str):
        self._text = text
        self._url = url

    def adapt(self) -> InlineKeyboardButton:
        return InlineKeyboardButton(self._text, url=self._url)


class InlineQueryButton:
    def __init__(self, text: str, query: str = ''):
        self._text = text
        self._query = query

    def adapt(self) -> InlineKeyboardButton:
        return InlineKeyboardButton(self._text, switch_inline_query_current_chat=self._query)


class InlineKeyboard:
    def __new__(cls, *args, **kwargs):
        obj = super().__new__(cls)
        obj._raw = InlineKeyboardMarkup()
        return obj

    def add_row(self, *buttons: CallbackButton | UrlButton | InlineQueryButton):
        raw_buttons = [button.adapt() for button in buttons]
        self._raw.row(*raw_buttons)

    def add_rows(self, *buttons: CallbackButton | UrlButton | InlineQueryButton):
        for button in buttons:
            self.add_row(button)

    def adapt(self) -> InlineKeyboardMarkup:
        return self._raw
