from telebot import types
from threading import Lock


class KeyBordUtils:
    """Утилит с клавиатурами"""

    @staticmethod
    def markups():
        markup = types.InlineKeyboardMarkup()
        btn_add_doc = types.InlineKeyboardButton(
            "➕Добавить док", callback_data="add_doc"
        )
        btn_search_in_docs = types.InlineKeyboardButton(
            "🔍Поиск по докам", callback_data="search_in_docs"
        )
        btn_manage = types.InlineKeyboardButton("🛠Управление", callback_data="manage")
        markup.row(btn_add_doc, btn_search_in_docs)
        markup.row(btn_manage)
        return markup

    @staticmethod
    def markups_back():
        markup = types.InlineKeyboardMarkup()
        btn_back = types.InlineKeyboardButton("🔙обратно", callback_data="back")
        markup.row(btn_back)
        return markup

    @staticmethod
    def markups_manage():
        markup = types.InlineKeyboardMarkup()
        btn_manage1 = types.InlineKeyboardButton("Изменение 1", callback_data="change1")
        btn_manage2 = types.InlineKeyboardButton("Изменение 2", callback_data="change2")
        btn_manage3 = types.InlineKeyboardButton("Изменение 3", callback_data="change3")
        markup.row(btn_manage1, btn_manage2)
        markup.row(btn_manage3)
        return markup
