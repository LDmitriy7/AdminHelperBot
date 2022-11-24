from assets import commands, states
from core import events

start = events.Command(commands.ADD_SALE)
channels = events.Text(state=states.AddingSale.channels)
date = events.Text(state=states.AddingSale.date)
time = events.Text(state=states.AddingSale.time)
