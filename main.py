from conf import bot_views, bot_logic, bot_core
import io
from fastapi import UploadFile
from telebot import types
from src.States import MyStates
from src.command_handler import *

BOT = bot_core.bot
print(f"{id(BOT)} - main")

@BOT.message_handler(commands=["start"])
def start(message):
    BOT.set_state(message.from_user.id, MyStates.start)
    bot_views.start(message)
    BOT.set_state(message.from_user.id, MyStates.main_menu)


@BOT.message_handler(commands=["menu"])
def menu(message):
    BOT.set_state(message.from_user.id, MyStates.main_menu)
    bot_views.menu()


async def add_file(m):
    pass


@BOT.message_handler(
    content_types=["document"],
    state=MyStates.wait_document,  # Только когда ждем документ
)
async def handle_telegram_document(message: types.Message):
    """Принимает документ из Telegram и передает в обработчик add_file"""
    try:
        # Получаем файл из Telegram
        file_info = BOT.get_file(message.document.file_id)
        file_data = BOT.download_file(file_info.file_path)

        # Создаем объект UploadFile, который ожидает add_file
        upload_file = UploadFile(
            filename=message.document.file_name,
            file=io.BytesIO(file_data),
            size=message.document.file_size,
        )

        # Передаем в вашу функцию обработки
        result = await add_file(upload_file)

        # Отправляем результат пользователю
        BOT.reply_to(message, f"😺 Файл успешно обработан!\nРезультат: {result}")

    except Exception as e:
        BOT.reply_to(message, f"😿 Ошибка обработки файла: {str(e)}")
        raise

    finally:
        BOT.set_state(message.from_user.id, MyStates.main_menu)
        bot_views.menu()


@BOT.message_handler(state=MyStates.wait_search, content_types=["text"])
def handle_search_query(message):
    bot_logic._search(message)



@BOT.message_handler(content_types=["text"])
def check_message(message):
    """Функция для проверки на случайные сообщения пользователя(которые не относятся к командам)"""
    current_state = BOT.get_state(message.from_user.id)
    if current_state in [MyStates.wait_document.name, MyStates.wait_search.name]:
        return

    if not message.text.startswith("/"):
        bot_views.answer_invalid_message()
    else:
        bot_views.answer_invalid_command()


@BOT.callback_query_handler(func=lambda callback: True)
def handler(callback: types.CallbackQuery):
    """Функция, которая обрабатывает каллбеки и выполняет логику бота"""
    if callback.data == "menu":
        bot_views.menu()
        BOT.delete_message(bot_views.user_id, callback.message.id)
    elif callback.data == "add_doc":
        bot_logic.add_doc()  # добавления дока
        bot_views.delete_last_msg(callback.message.id)
    elif callback.data == "search_in_docs":
        BOT.set_state(callback.from_user.id, MyStates.wait_search)
        bot_logic.ask_request(callback.message)  # генерирует ответ по запросу в доках
        bot_views.delete_last_msg(callback.message.id)
        print(f"Состояние после set_state: {BOT.get_state(callback.from_user.id)}")
    elif callback.data == "manage":
        bot_logic.manage()  # управление/редактирование дока
        bot_views.delete_last_msg(callback.message.id)
    elif callback.data == "back":
        bot_views.menu()
        bot_views.delete_last_msg(callback.message.id)
    elif callback.data == "change1":
        bot_views.answer_on_manage_end()
    elif callback.data == "change2":
        bot_views.answer_on_manage_end()
    elif callback.data == "change3":
        bot_views.answer_on_manage_end()


BOT.polling(non_stop=True)
