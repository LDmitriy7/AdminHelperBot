import actions.add_sale as actions
import events.add_sale as events
from core import HandlerGroup, Handler

ADD_SALE = HandlerGroup(
    Handler(events.start, actions.ask_channels),
    Handler(events.pick_channel, actions.pick_channel),
    Handler(events.pick_all_channels,actions.pick_all_channels),
    Handler(events.channels_finish, actions.ask_date),
    Handler(events.date, actions.ask_time),
    Handler(events.time, actions.finish),
)
