from assets import commands
from core import events
from . import add_sale

start = events.Command(commands.START, state='*')
test = events.Command(commands.TEST, state='*')
channels = events.Command(commands.CHANNELS, state='*')
