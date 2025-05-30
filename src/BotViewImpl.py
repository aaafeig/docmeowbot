from .interface import BotView
from .Utils import KeyBordUtils
from .BaseBot import BotBase, BotCore


class BotViewImpl(BotBase, BotView):
    def __init__(self, token: str, core: BotCore):
        super().__init__(token, core)
        self.__markups = KeyBordUtils.markups()

    def start(self, message):
        """Метод для вывода начального сообщения"""
        self._core.user_id = message.chat.id
        markup = self.__markups
        self._bot.send_message(self._core.user_id, "😼Мяу! это docmeowbot😼, который может делать поиск по документам, хоть у меня лапки🐾!", reply_markup=markup)

    def menu(self):
        """Метод для вывода меню"""
        markup = self.__markups
        self._bot.send_message(self._core.user_id, "Выбери действие, мурр", reply_markup=markup)

    def answer_invalid_message(self):
        """Метод для вывода сообщения-предупреждения"""
        self._bot.send_message(self._core.user_id, "Я котик и понимаю только команды😿")

    def answer_invalid_command(self):
        """Метод для вывода сообщения-предупреждения"""
        self._bot.send_message(self._core.user_id, "Я еще не выучил эту команду😿")