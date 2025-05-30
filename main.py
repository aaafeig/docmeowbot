from conf import  bot_views, bot_logic
import io
from fastapi import UploadFile
from telebot import types

BOT = bot_views.bot

async def add_file(m):
    pass

@BOT.message_handler(content_types=['document'])
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
            size=message.document.file_size
        )

        # Передаем в вашу функцию обработки
        result = await add_file(upload_file)

        # Отправляем результат пользователю
        BOT.reply_to(message, f"😺 Файл успешно обработан!\nРезультат: {result}")

    except Exception as e:
        BOT.reply_to(message, f"😿 Ошибка обработки файла: {str(e)}")
        raise

    finally:
        bot_views.menu()

@BOT.message_handler(func=lambda message: True, content_types=['text'])
def check_message(message):
    """Функция для проверки на случайные сообщения пользователя(которые не относятся к командам)"""
    if not message.text.startswith('/'):
        bot_views.answer_invalid_message()
    else:
        bot_views.answer_invalid_command()


@BOT.callback_query_handler(func=lambda callback: True)
def handler(callback):
    """Функция, которая обрабатывает каллбеки и выполняет логику бота"""
    if callback.data == "add_doc":
        bot_logic.add_doc() # добавления дока
    elif callback.data == "search_in_docs":
        bot_logic.search() #генерирует ответ по запросу в доках
    elif callback.data == "manage": # управление/редактирование дока
        bot_logic.manage()
    elif callback.data == "back":
        bot_views.menu()
BOT.polling(non_stop=True)