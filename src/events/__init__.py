from assets import kbs, states
from core import events

start = events.Command('start', state='*')
test = events.Command('test', state='*')

clients_chat = events.Click(kbs.MainMenu.clients_chat)
to_main_menu = events.Click(kbs.MAIN_MENU_BUTTON)
store_rules = events.Click(kbs.MainMenu.store_rules)
cities_list = events.Click(kbs.MainMenu.cities_list)

search_city = events.InlineQuery()
city_via_search = events.Text(via_bot=True)

region = events.Text(state=states.Order.region)

refill_order = events.Text(kbs.ConfirmOrder.refill_order, state=states.Order.confirmation)
check_payment = events.Text(kbs.CheckPayment.check_payment, state=states.Order.payment)
