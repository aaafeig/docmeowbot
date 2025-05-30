from abc import  ABC, abstractmethod
import telebot


class BotCore:
    """Класс для хранения общих данных бота"""

    def __init__(self):
        self._user_id = None
        
    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, new_id):
        self._user_id = new_id


class BotBase(ABC):
    """Абстрактный базовый класс с зависимостью от BotCore"""

    def __init__(self, token: str, core: BotCore):
        self._token = token
        self._bot = telebot.TeleBot(token)
        self._core = core

    @property
    def user_id(self):
        """Доступ к общему user_id через BotCore"""
        return self._core.user_id

    @user_id.setter
    def user_id(self, new_id):
        self._core.user_id = new_id

    @property
    def bot(self):
        return self._bot
