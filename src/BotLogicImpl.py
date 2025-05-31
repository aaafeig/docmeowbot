from telebot import types
from .interface import BotLogic
from .BaseBot import BotBase, BotCore
from .Utils import KeyBordUtils
from .States import MyStates


class BotLogicImpl(BotBase, BotLogic):
    """Класс для работы, который отвечает за логику"""

    def __init__(self, token: str, core: BotCore):
        super().__init__(token, core)
        self._back_markups = KeyBordUtils.markups_back()
        self._manager_markups = KeyBordUtils.markups_manage()

    async def add_doc(self, doc):
        """Метод для добавления файла в БД"""
        self.bot.send_message(
            self._core.user_id,
            "🐱Скинь мне свой файл формата PDF, DOCX, Markdown или TXT",
        )

    def ask_request(self, message: types.Message):
        self._core.user_id = message.chat.id
        print(self._core.user_id)
        self.bot.set_state(self._core.user_id, MyStates.wait_search)
        self.bot.send_message(self._core.user_id, "Что мне искать?")

    def _search(self, message: types.Message):
        """Метод для поиска по базе"""
        print(message)
        if not message.text:
            self.bot.send_message(self._core.user_id, "Введите текстовый запрос")
            return

        markup = self._back_markups
        self.bot.send_message(
            self._core.user_id,
            f"🐾Выполняю поиск по запросу  '{message.text}' в базе...",
        )
        self.bot.send_message(self._core.user_id, "😽Готово!", reply_markup=markup)
        self.bot.delete_state(message.from_user.id)

    def manage(self):
        """Метод для управления файлом"""
        markup = self._manager_markups
        self.bot.send_message(
            self._core.user_id, "Что мне надо сделать?", reply_markup=markup
        )
