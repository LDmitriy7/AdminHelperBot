import actions
import events
from core import HandlerGroup, Handler

TEST = HandlerGroup(
    Handler(events.test, actions.test),
)
