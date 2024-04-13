from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext

from TelegramBot.keyboards import start_keyboards
from TelegramBot.DataBase import create_db_user, set_data, get_data
from TelegramBot.MemoryCodeApi.main import authentication


async def start_message(msg: types.Message) -> None:
    """
    Сообщение, которое выводится при старте бота

    :param msg: Объект сообщения
    """
    await msg.delete()
    name = msg.from_user.first_name
    chat_id = msg.chat.id
    create_db_user("users", name, chat_id)

    await msg.answer(f"Привет, {name}! Я помогу тебе заполнить поля для хакатона",
                     reply_markup=start_keyboards.start_button())


async def get_nickname(msg: types.Message, state: FSMContext) -> None:
    """
    Функция, в которой мы получаем логин пользователя для входа на сайт

    :param msg: Объект сообщения
    :param state: Текущее состояние
    """
    sent_message = await msg.message.edit_text("Напиши свой логин от сайта")
    await state.update_data(sent_message_id=sent_message.message_id)
    await state.set_state("waiting_get_pass")


async def get_pass(msg: types.Message, state: FSMContext) -> None:
    """
    Функция, которая вызывается после того, как пользователь отправил
    ответ на сообщение "Напиши свой логин от сайта" В эту функцию мы переходим
    с состоянием FSM: login_site

    :param msg: Объект сообщения
    :param state: Текущее состояние FSM
    """
    data = await state.get_data()
    sent_message_id = data.get("sent_message_id")

    set_data("users", "login", msg.text, "chatID", msg.chat.id)

    sent_message = await msg.bot.edit_message_text(chat_id=msg.chat.id, message_id=sent_message_id,
                                                   text="Пароль для входа")
    await state.update_data(sent_message_id=sent_message.message_id)
    await state.set_state("login_site")
    await msg.delete()


async def check_login(msg: types.Message, state: FSMContext) -> None:
    """
    Функция, которая отвечает за проверку вводимых данных. В случае, если
    email и password введены верно, мы полуаем токен и переходим к изменению
    страницы. В ином случае бот сообщает нам, что данные не корректны
    и предлагает войти в аккаунт снова

    :param msg: Объект сообщения
    :param state: Текущее состояние FSM
    """
    data = await state.get_data()
    sent_message_id = data.get("sent_message_id")

    set_data("users", "pass", msg.text, "chatID", msg.chat.id)

    await state.set_state("check_logining")

    email = get_data("users", "login", "chatID", msg.chat.id)[0][0]
    password = get_data("users", "pass", "chatID", msg.chat.id)[0][0]

    is_authenticated = authentication(email, password)
    if is_authenticated:
        set_data('users', 'token', is_authenticated, 'chatID', msg.chat.id)
        sent_message = await msg.bot.edit_message_text(chat_id=msg.chat.id, message_id=sent_message_id,
                                                       text="Аутентификация успешна.",
                                                       reply_markup=start_keyboards.edit_info())
        await state.update_data(sent_message_id=sent_message.message_id)
        await state.finish()
    else:
        sent_message = await msg.bot.edit_message_text(chat_id=msg.chat.id, message_id=sent_message_id,
                                                       text="Неверные учетные данные. Попробуйте снова.",
                                                       reply_markup=start_keyboards.start_button())
        await state.update_data(sent_message_id=sent_message.message_id)
        await state.finish()
    await msg.delete()


async def check_signin(msg: types.Message):
    """
       Функция, которая отвечает за проверку вводимых данных. В случае, если
       email и password введены верно, мы полуаем токен и переходим к изменению
       страницы. В ином случае бот сообщает нам, что данные не корректны
       и предлагает войти в аккаунт снова

       :param msg: Объект сообщения
       """

    email = get_data("users", "login", "chatID", msg.message.chat.id)[0][0]
    password = get_data("users", "pass", "chatID", msg.message.chat.id)[0][0]

    is_authenticated = authentication(email, password)
    if is_authenticated:
        set_data('users', 'token', is_authenticated, 'chatID', msg.message.chat.id)
        await msg.message.edit_text("Вход произведен успешно", reply_markup=start_keyboards.edit_info())
    else:
        await msg.message.edit_text("Вхрд не выполнен. Поробуйте авторизоваться заново", reply_markup=start_keyboards.start_button())


def start_handler(dp: Dispatcher) -> None:
    """
     Функция, в которой мы описываем, как вызываются функции для взаимодействия
     в тг боте
     """
    dp.register_message_handler(start_message, commands=['start'])
    dp.register_callback_query_handler(get_nickname,
                                       lambda s: s.data == "login")
    dp.register_message_handler(get_pass, state="waiting_get_pass")
    dp.register_message_handler(check_login, state="login_site")
    dp.register_callback_query_handler(check_signin, lambda s: s.data == "signin")
