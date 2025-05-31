from main import BOT
from conf import bot_views, bot_logic


@BOT.message_handler(commands=["menu"])
def menu():
    bot_views.menu()


@BOT.message_handler(commands=["docadd"])
def add_doc():
    bot_logic.add_doc()


@BOT.message_handler(commands=["searchindoc"])
def search_in_doc():
    bot_logic.search()


@BOT.message_handler(commands=["managedoc"])
def manage_doc():
    bot_logic.manage()
