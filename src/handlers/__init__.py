from core import HandlerGroup
from .start import START
from .test import TEST
from .add_sale import ADD_SALE

HANDLERS = HandlerGroup(
    START,
    ADD_SALE,
    TEST,
)
