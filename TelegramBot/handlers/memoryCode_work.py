import json

from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext

from TelegramBot.MemoryCodeApi import personal_info, main
from TelegramBot.DataBase import base_workDB
from TelegramBot.bot_configure import bot
from TelegramBot.keyboards import memoryCode_keyboards
from Epitaph import ai_agents_epitaph


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
    num_page = int(msg.text)
    base_workDB.set_data('users', 'page', num_page, 'chatID', msg.chat.id)
    token = base_workDB.get_data("users", 'token',
                                 'chatID', msg.chat.id)[0][0]

    text = personal_info.get_full_info(token, num_page - 1)

    if text is None:
        text = "Страница не найдена"

    await msg.delete()
    sent_message = await bot.edit_message_text(chat_id=msg.chat.id, message_id=sent_message_id,
                                               text=text, reply_markup=memoryCode_keyboards.edit_or_ok())
    await state.update_data(sent_message_id=sent_message.message_id)
    await state.finish()


async def brief_info(msg: types.Message, state: FSMContext) -> None:
    text = "Введите место рождения"
    sent_message = await bot.send_message(msg.message.chat.id, text)

    await state.update_data(sent_message_id=sent_message.message_id)
    await state.set_state("place_birth")


async def place_birth(msg: types.Message, state: FSMContext) -> None:
    text = "Введите место смерти"
    base_workDB.set_data('users', 'place_birth', msg.text, 'chatID', msg.chat.id)

    await msg.delete()
    data = await state.get_data()
    sent_message_id = data.get("sent_message_id")
    sent_message = await bot.edit_message_text(chat_id=msg.chat.id, message_id=sent_message_id,
                                               text=text)

    await state.update_data(sent_message_id=sent_message.message_id)
    await state.set_state("place_die")


async def place_die(msg: types.Message, state: FSMContext) -> None:
    text = 'Есть ли дети? Если да - то укажите имя, если нет - то напишите "детей нет"'
    base_workDB.set_data('users', 'place_die', msg.text, 'chatID', msg.chat.id)

    await msg.delete()
    data = await state.get_data()
    sent_message_id = data.get("sent_message_id")
    sent_message = await bot.edit_message_text(chat_id=msg.chat.id, message_id=sent_message_id,
                                               text=text)

    await state.update_data(sent_message_id=sent_message.message_id)
    await state.set_state("child_info")


async def child(msg: types.Message, state: FSMContext) -> None:
    text = 'Есть ли супруг или супруга? Информация укажите, как в предудущем пункте)'
    base_workDB.set_data('users', 'child', msg.text, 'chatID', msg.chat.id)

    await msg.delete()
    data = await state.get_data()
    sent_message_id = data.get("sent_message_id")
    sent_message = await bot.edit_message_text(chat_id=msg.chat.id, message_id=sent_message_id,
                                               text=text)

    await state.update_data(sent_message_id=sent_message.message_id)
    await state.set_state("spouse_info")


async def spouse(msg: types.Message, state: FSMContext) -> None:
    text = 'Укажите гражданство'
    base_workDB.set_data('users', 'spouse', msg.text, 'chatID', msg.chat.id)

    await msg.delete()
    data = await state.get_data()
    sent_message_id = data.get("sent_message_id")
    sent_message = await bot.edit_message_text(chat_id=msg.chat.id, message_id=sent_message_id,
                                               text=text)

    await state.update_data(sent_message_id=sent_message.message_id)
    await state.set_state("nationaly_info")


async def nationaly(msg: types.Message, state: FSMContext) -> None:
    text = 'Укажите образование'
    base_workDB.set_data('users', 'nationally', msg.text, 'chatID', msg.chat.id)

    await msg.delete()
    data = await state.get_data()
    sent_message_id = data.get("sent_message_id")
    sent_message = await bot.edit_message_text(chat_id=msg.chat.id, message_id=sent_message_id,
                                               text=text)

    await state.update_data(sent_message_id=sent_message.message_id)
    await state.set_state("study_info")


async def study(msg: types.Message, state: FSMContext) -> None:
    text = 'Укажите род деятельности'
    base_workDB.set_data('users', 'study', msg.text, 'chatID', msg.chat.id)

    await msg.delete()
    data = await state.get_data()
    sent_message_id = data.get("sent_message_id")
    sent_message = await bot.edit_message_text(chat_id=msg.chat.id, message_id=sent_message_id,
                                               text=text)

    await state.update_data(sent_message_id=sent_message.message_id)
    await state.set_state("job_info")


async def job(msg: types.Message, state: FSMContext) -> None:
    text = 'Укажите награды/премии и достижения'
    base_workDB.set_data('users', 'job', msg.text, 'chatID', msg.chat.id)

    await msg.delete()
    data = await state.get_data()
    sent_message_id = data.get("sent_message_id")
    sent_message = await bot.edit_message_text(chat_id=msg.chat.id, message_id=sent_message_id,
                                               text=text)

    await state.update_data(sent_message_id=sent_message.message_id)
    await state.set_state("award_info")


async def award(msg: types.Message, state: FSMContext) -> None:
    text = 'Как заполянем дальше?'
    base_workDB.set_data('users', 'award', msg.text, 'chatID', msg.chat.id)

    await msg.delete()
    data = await state.get_data()
    sent_message_id = data.get("sent_message_id")
    sent_message = await bot.edit_message_text(chat_id=msg.chat.id, message_id=sent_message_id,
                                               text=text, reply_markup=memoryCode_keyboards.choice_method())

    await state.update_data(sent_message_id=sent_message.message_id)
    await state.finish()


async def ai_generate_epitaph(msg: types.Message) -> None:
    job = base_workDB.get_data("users", "job", "chatID", msg.message.chat.id)[0][0]
    awards = base_workDB.get_data("users", "award", "chatID", msg.message.chat.id)[0][0]
    page = base_workDB.get_data("users", "page", "chatID", msg.message.chat.id)
    token = base_workDB.get_data("users", "token", "chatID", msg.message.chat.id)
    full_name = personal_info.get_full_info(token[0][0], page[0][0] - 1).split('\n')[1][5:]
    new_ai_text = [full_name, job, awards]

    js_string = personal_info.get_json_string()
    new_js_str = personal_info.replace_user_texts(js_string, new_ai_text)
    ai_ep = ai_agents_epitaph.gpt(new_js_str)
    ai_an = ai_agents_epitaph.analyzerAgentGpt(ai_ep)
    result_json = json.loads(ai_an)
    text = result_json['result']['alternatives'][0]['message']['text']

    if len(text) > 300:
        ai_an = ai_agents_epitaph.rewriterAgentGpt(ai_an)
        ai_ahalyser = ai_agents_epitaph.analyzerAgentGpt(ai_an)
        result_json = json.loads(ai_ahalyser)
        text = result_json['result']['alternatives'][0]['message']['text']

    main.fill_data(text, token[0][0], page[0][0] - 1)
    await msg.message.edit_text(text, reply_markup=memoryCode_keyboards.regenerate())


def memoryCode_handler(dp: Dispatcher) -> None:
    """
     Функция, в которой мы описываем, как вызываются функции для взаимодействия
     в тг боте
     """
    dp.register_callback_query_handler(choice_page,
                                       lambda s: s.data == "choice_page")
    dp.register_message_handler(person_choice, state="person_choice")
    dp.register_callback_query_handler(brief_info, lambda s: s.data == "edit_person")
    dp.register_message_handler(place_birth, state="place_birth")
    dp.register_message_handler(place_die, state="place_die")
    dp.register_message_handler(child, state="child_info")
    dp.register_message_handler(spouse, state="spouse_info")
    dp.register_message_handler(nationaly, state="nationaly_info")
    dp.register_message_handler(study, state="study_info")
    dp.register_message_handler(job, state="job_info")
    dp.register_message_handler(award, state="award_info")
    dp.register_callback_query_handler(ai_generate_epitaph, lambda s: s.data in ["edit_ai", "regenerate"])
