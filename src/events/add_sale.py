from assets import commands, states, kbs
from core import events

start = events.Command(commands.ADD_SALE)
date = events.Text(state=states.AddingSale.date)
time = events.Text(state=states.AddingSale.time)
pick_channel = events.Click(kbs.Channels.item, state=states.AddingSale.channels)
pick_all_channels = events.Click(kbs.Channels.pick_all, state=states.AddingSale.channels)
channels_finish = events.Click(kbs.Channels.finish, state=states.AddingSale.channels)
