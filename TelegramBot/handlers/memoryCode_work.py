from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext

from TelegramBot.MemoryCodeApi import personal_info
from TelegramBot.DataBase import base_workDB
from TelegramBot.bot_configure import bot
from TelegramBot.keyboards import memoryCode_keyboards


async def choice_page(msg: types.Message, state: FSMContext) -> None:
    """
    Функция, в которой мы даём пользователю выбрать номер страницы,
    информацию которой он хочет поменять

    :param msg: Объект сообщения (callback)
    :param state: Текущее состояние FSM
    """
    token = base_workDB.get_data("users", 'token',
                                 'chatID', msg.message.chat.id)
    pers_info = personal_info.get_fullname_pages(token[0][0])

    if pers_info:
        text = ("Отправьте боту число - номер страницы, которую Вы "
                "хотите отредактировать\n")
        index = 0
        for info in pers_info:
            split_info = info.split("\n")
            full_name = split_info[0][1:]
            birthday = split_info[1]

            index += 1
            text += f'\nСтраница: {index}\n{full_name}\nДата рождения: {birthday}\n'
    else:
        text = 'Страницы не найдены'

    sent_message = await bot.send_message(msg.message.chat.id, text)

    await state.update_data(sent_message_id=sent_message.message_id)
    await state.set_state("person_choice")


async def person_choice(msg: types.Message, state: FSMContext) -> None:
    """
    В этой функии пользователь подтверждает выбор страницы, либо
    возвращается назад для смены выбора

    :param msg: Объект сообщения
    :param state: Текущее состояние FSM
    """
    data = await state.get_data()
    sent_message_id = data.get("sent_message_id")

    text = f"Выбранная станица: {msg.text}\n"

    await msg.delete()
    sent_message = await bot.edit_message_text(chat_id=msg.chat.id, message_id=sent_message_id,
                                               text=text, reply_markup=memoryCode_keyboards.edit_or_ok())
    await state.update_data(sent_message_id=sent_message.message_id)
    await state.finish()


async def edit_person_info(msg: types.Message) -> None:
    """
    В этой функии мы должны начинать менять информацию
    страницы, которую выбрал пользователь

    :param msg: Объект сообщения (callback)
    """
    await bot.send_message("123")


def memoryCode_handler(dp: Dispatcher) -> None:
    """
     Функция, в которой мы описываем, как вызываются функции для взаимодействия
     в тг боте
     """
    dp.register_callback_query_handler(choice_page,
                                       lambda s: s.data == "choice_page")
    dp.register_message_handler(person_choice, state="person_choice")
    dp.register_callback_query_handler(edit_person_info, callback="edit_person")
