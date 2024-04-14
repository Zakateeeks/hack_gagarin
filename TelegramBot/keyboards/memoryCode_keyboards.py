from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def edit_or_ok() -> InlineKeyboardMarkup:
    """
    Кнопки после выбора страницы для редактирования,
    пользователь либо подтверждает выбор, либо
    возвращается к списку страниц

    :return: inline клавиатура
    """
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(
        InlineKeyboardButton(text="Всё верно", callback_data="choice_page"),
        InlineKeyboardButton(text="Заполнить эту страницу", callback_data="edit_person")
    )

    return keyboard


def choice_method() -> InlineKeyboardMarkup:
    """
    Кнопки после подтверждения страницы для выбора метода редактирования,
    пользователь выбирает либо вручную, либо
    использовать AI

    :return: inline клавиатура
    """
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(
        InlineKeyboardButton(text="Использовать помощь AI", callback_data="edit_ai")
    )

    return keyboard

def regenerate() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(
        InlineKeyboardButton(text="Перегенерировать", callback_data="regenerate")
    )

    return keyboard
