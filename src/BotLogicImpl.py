from pickle import FRAME

from .interface import BotLogic
from .BaseBot import BotBase, BotCore
from .Utils import KeyBordUtils

class BotLogicImpl(BotBase, BotLogic):

    """Класс для работы, который отвечает за логику"""

    def __init__(self, token: str, core: BotCore):
        super().__init__(token, core)
        self._back_markups = KeyBordUtils.markups_back()

    def add_doc(self, doc):
        """Метод для добавления файла в БД"""
        markup = self._back_markups
        self._bot.send_message(self._core.user_id, "🐱Скинь мне свой файл формата PDF, DOCX, Markdown или TXT")
        self._bot.send_message(self._core.user_id, "😽Готово!", reply_markup=markup)
    def search(self, request: str):
        """Метод для поиска по базе"""
        markup = self._back_markups
        self._bot.send_message(self._core.user_id, f"🐾Выполняю поиск по запросу  {request} в базе...")
        self._bot.send_message(self._core.user_id, "😽Готово!", reply_markup=markup)

    def manage(self):
        """Метод для управления файлом"""
        markup = self._back_markups
        self._bot.send_message(self._core.user_id, "🧶Управляю твоим файлом...")
        self._bot.send_message(self._core.user_id, "😽Готово!", reply_markup=markup)
