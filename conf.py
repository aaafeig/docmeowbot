import os

from dotenv import load_dotenv

from src.BaseBot import BotCore
from src.BotViewImpl import BotViewImpl
from src.BotLogicImpl import BotLogicImpl

load_dotenv()
token = os.getenv('YOUR_TOKEN')
bot_core = BotCore(token)
bot_logic = BotLogicImpl(bot_core)
bot_views = BotViewImpl(bot_core)
