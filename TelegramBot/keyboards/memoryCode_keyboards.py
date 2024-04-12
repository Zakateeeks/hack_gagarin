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
        InlineKeyboardButton(text="Всё верно", callback_data="edit_person"),
        InlineKeyboardButton(text="Другая страница", callback_data="choice_page")
    )

    return keyboard
