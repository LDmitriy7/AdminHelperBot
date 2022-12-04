from core import HandlerGroup
from .finish import FINISH
from .pick import PICK
from .pick_all import PICK_ALL

CHANNELS = HandlerGroup(
    PICK,
    PICK_ALL,
    FINISH,
)
