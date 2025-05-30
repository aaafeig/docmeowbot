from .interface import Bot
import telebot

class BotImpl(Bot):

    def __init__(self, bot: telebot):
        self.bot = bot

    def start(self):
        pass

    def menu(self):
        pass