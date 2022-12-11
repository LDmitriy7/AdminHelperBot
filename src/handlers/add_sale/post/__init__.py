from core import HandlerGroup
from .messages import MESSAGES
from .skip import SKIP

POST = HandlerGroup(
    SKIP,
    MESSAGES,
)
