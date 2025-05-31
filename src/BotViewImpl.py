from .interface import BotView
from .Utils import KeyBordUtils
from .BaseBot import BotBase, BotCore
from telebot import types


class BotViewImpl(BotBase, BotView):
    def __init__(self, token: str, core: BotCore):
        super().__init__(token, core)
        self.__markups = KeyBordUtils.markups()
        self._back_markups = KeyBordUtils.markups_back()

    def start(self, message: types.Message):
        """Метод для вывода начального сообщения"""
        self._core.user_id = message.chat.id
        print(self._core.user_id)
        markup = self.__markups
        self.bot.send_message(
            self._core.user_id,
            "😼Мяу! это docmeowbot😼, который может делать поиск по документам, хоть у меня лапки🐾!",
            reply_markup=markup,
        )

    def menu(self):
        """Метод для вывода меню"""
        markup = self.__markups
        self.bot.send_message(
            self._core.user_id, "Выбери действие, мурр", reply_markup=markup
        )

    def answer_invalid_message(self):
        """Метод для вывода сообщения-предупреждения"""
        self.bot.send_message(self._core.user_id, "Я котик и понимаю только команды😿")

    def answer_invalid_command(self):
        """Метод для вывода сообщения-предупреждения"""
        self.bot.send_message(self._core.user_id, "Я еще не выучил эту команду😿")

    def answer_on_manage_end(self):
        markup = self._back_markups
        self.bot.send_message(self._core.user_id, "🧶Управляю твоим файлом...")
        self.bot.send_message(self._core.user_id, "😽Готово!", reply_markup=markup)

    def delete_last_msg(self, msg_id: int):
        self.bot.delete_message(self._core.user_id, msg_id)
