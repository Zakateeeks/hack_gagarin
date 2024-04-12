from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def start_button() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(
        InlineKeyboardButton(text="Войти", callback_data="login")
    )

    return keyboard
