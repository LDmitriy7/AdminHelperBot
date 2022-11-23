from core import HandlerGroup
from .start import START
from .test import TEST

HANDLERS = HandlerGroup(
    START,
    TEST,
)
