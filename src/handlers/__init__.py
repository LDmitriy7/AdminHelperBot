from core import HandlerGroup
from .add_sale import ADD_SALE
from .channels import CHANNELS
from .start import START
from .test import TEST

HANDLERS = HandlerGroup(
    START,
    CHANNELS,
    ADD_SALE,
    TEST,
)
