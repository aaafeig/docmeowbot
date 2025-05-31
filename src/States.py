from telebot.handler_backends import StatesGroup, State


class MyStates(StatesGroup):
    start = State()  # После команды /start
    wait_document = State()  # Ожидаем документ
    wait_search = State()  # Ожидаем поисковый запрос
    main_menu = State()  # Основное меню
