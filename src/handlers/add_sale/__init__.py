from core import HandlerGroup
from .channels import CHANNELS
from .date import DATE
from .start import START
from .time import TIME
from .post import POST

ADD_SALE = HandlerGroup(
    START,
    CHANNELS,
    DATE,
    TIME,
    POST,
)
