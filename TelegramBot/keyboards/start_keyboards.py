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
        InlineKeyboardButton(text="Войти", callback_data="login")
    )

    return keyboard


def edit_info() -> InlineKeyboardMarkup:
    """
    Кнопка после успешной авторизации

    :return: inline клавиатура
    """

    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(
        InlineKeyboardButton(text="Редактировать страницу",
                             callback_data="edit_page")
    )

    return keyboard
