import actions
import events
from core import HandlerGroup, Handler

START = HandlerGroup(
    Handler(events.start, actions.start),
)
