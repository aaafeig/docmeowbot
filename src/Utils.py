from telebot import types

class KeyBordUtils:

    @staticmethod
    def markups():
        markup = types.InlineKeyboardMarkup()
        btn_add_doc = types.InlineKeyboardButton("➕Добавить док", callback_data="add_doc")
        btn_search_in_docs = types.InlineKeyboardButton("🔍Поиск по докам", callback_data="search_in_docs")
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


