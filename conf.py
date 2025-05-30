import os

from dotenv import load_dotenv

from src.BaseBot import BotCore
from src.BotViewImpl import BotViewImpl
from src.BotLogicImpl import BotLogicImpl

load_dotenv()
token = os.getenv('YOUR_TOKEN')
bot_core = BotCore()
bot_logic = BotLogicImpl(token, bot_core)
bot_views = BotViewImpl(token, bot_core)
