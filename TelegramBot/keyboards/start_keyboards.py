from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def start_button() -> InlineKeyboardMarkup:
    """
    Кнопка на стартовом сообщении
    После её нажатия нас отправляет в FSM для
    ввода данных для входа

    :return: inline клавиатура
    """
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(
        InlineKeyboardButton(text="Авторизоваться", callback_data="login"),
        InlineKeyboardButton(text="Войти", callback_data="signin")
    )

    return keyboard


def edit_info() -> InlineKeyboardMarkup:
    """
    Кнопка после успешной авторизации

    :return: inline клавиатура
    """

    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(
        InlineKeyboardButton(text="Выбрать страницу",
                             callback_data="choice_page")
    )

    return keyboard
