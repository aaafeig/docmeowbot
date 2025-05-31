from abc import ABC
import telebot
from telebot.storage import StateMemoryStorage


from telebot import TeleBot
from telebot.storage import StateMemoryStorage

class BotCore:
    """Класс для хранения общих данных бота и единого экземпляра TeleBot"""
    def __init__(self, token: str):
        self._user_id = None
        self.storage = StateMemoryStorage()
        self._bot = TeleBot(token, state_storage=self.storage)

    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, new_id):
        self._user_id = new_id

    @property
    def bot(self):
        return self._bot


class BotBase(ABC):
    """Абстрактный базовый класс с зависимостью от BotCore"""
    def __init__(self, core: BotCore):
        self._core = core

    @property
    def user_id(self):
        return self._core.user_id

    @user_id.setter
    def user_id(self, new_id):
        self._core.user_id = new_id

    @property
    def bot(self):
        return self._core.bot
