from .interface import BotView
from .Utils import KeyBordUtils
from .BaseBot import BotBase, BotCore
from telebot import types


class BotViewImpl(BotBase, BotView):
    def __init__(self, core: BotCore):
        super().__init__(core)
        self.__markups = KeyBordUtils.markups()
        self._back_markups = KeyBordUtils.markups_back()


    def start(self, message: types.Message):
        """Метод для вывода начального сообщения"""
        self.user_id = message.chat.id
        print(self.user_id)
        markup = self.__markups
        self.bot.send_message(
            self.user_id,
            "😼Мяу! это docmeowbot😼, который может делать поиск по документам, хоть у меня лапки🐾!",
            reply_markup=markup,
        )

    def menu(self):
        """Метод для вывода меню"""
        markup = self.__markups
        self.bot.send_message(
            self.user_id, "Выбери действие, мурр", reply_markup=markup
        )

    def answer_invalid_message(self):
        """Метод для вывода сообщения-предупреждения"""
        markup = types.InlineKeyboardMarkup()
        btn_menu = types.InlineKeyboardButton("В меню", callback_data="menu")
        markup.row(btn_menu)
        self.bot.send_message(self.user_id, "Я котик и понимаю только команды😿", reply_markup=markup)


    def answer_invalid_command(self):
        """Метод для вывода сообщения-предупреждения"""
        markup = types.InlineKeyboardMarkup()
        btn_menu = types.InlineKeyboardButton("В меню", callback_data="menu")
        markup.row(btn_menu)
        self.bot.send_message(self.user_id, "Я еще не выучил эту команду😿", reply_markup=markup)

    def answer_on_manage_end(self):
        markup = self._back_markups
        self.bot.send_message(self.user_id, "🧶Управляю твоим файлом...")
        self.bot.send_message(self.user_id, "😽Готово!", reply_markup=markup)

    def delete_last_msg(self, msg_id: int):
        self.bot.delete_message(self.user_id, msg_id - 1)
        self.bot.delete_message(self.user_id, msg_id)
