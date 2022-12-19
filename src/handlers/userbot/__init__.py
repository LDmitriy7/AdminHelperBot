from core import HandlerGroup
from .phone_code import PHONE_CODE
from .start import START

USERBOT = HandlerGroup(
    START,
    PHONE_CODE,
)
