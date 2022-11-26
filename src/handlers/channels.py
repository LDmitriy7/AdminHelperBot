import actions
import events
from core import HandlerGroup, Handler

CHANNELS = HandlerGroup(
    Handler(events.channels, actions.show_channels),
)
