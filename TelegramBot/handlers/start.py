from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext


async def start_message(msg: types.Message) -> None:
    """
    Сообщение, которое выводится при старте бота

    :param msg: Адрес сообщения
    """

    await msg.answer("Привет! Я помогу тебе заполнить поля для хакатона")


async def get_user_name(msg: types.Message, state: FSMContext) -> None:
    """
    Сообщение, которое (на данный момент) выводится после нажатия на inline
    кнопку (если смотреть функцию хендера) и подключает FSM с начальным
    состоянием

    :param msg: Адрес сообщения
    :param state: Текущее состояние
    """

    sent_message = await msg.message.edit_text("Как тебя зовут?")
    await state.update_data(sent_message_id=sent_message.message_id)
    await state.set_state("waiting_get_city")


async def get_city_info(msg: types.Message, state: FSMContext) -> None:
    """
    Функция, которая вызывается после того, как пользователь отправил
    сообщение на ответ "Как тебя зовут?" В эту функцию мы переходим
    с состоянием FSM: waiting_get_city

    :param msg: Адрес сообщения
    :param state: Текущее состояние FSM
    """
    data = await state.get_data()
    sent_message_id = data.get("sent_message_id")

    sent_message = await msg.bot.edit_message_text(chat_id=msg.chat.id, message_id=sent_message_id,
                                                   text="В каком городе ты живешь?")
    await state.update_data(sent_message_id=sent_message.message_id)
    await state.set_state("waiting_eshe_chtoto")
    await msg.delete()


def start_handler(dp: Dispatcher) -> None:
    """
    Функция, в которой мы описываем, как вызываются функции для взаимодействия
    в тг боте
    """
    dp.register_message_handler(start_message, commands=['start'])
    dp.register_callback_query_handler(get_user_name, lambda s: s.data == "SSD") #Это получение данных из inline кнопки
    dp.register_message_handler(get_city_info, state="waiting_get_city")
