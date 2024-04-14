import requests
import json


def get_fullname_pages(access_token: str) -> list | None:
    """
    Функция для get запроса через API, получает информацию о
    полном имени человека со страницы и его дату рождения

    :param access_token: Токен доступа, получается после
    успешной авторизации и записывается в БД
    :return: Список страниц с нужной ифнормацией
    """
    url = "https://mc.dev.rand.agency/api/cabinet/individual-pages"

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json;charset=UTF-8",
        "Authorization": f"Bearer {access_token}"
    }

    response = requests.get(url, headers=headers)
    person_info_list = []

    if response.status_code == 200:
        for page in response.json():
            person_info_list.append(f"{page["full_name"]} \n {page["birthday_at"]}")
        return person_info_list
    else:
        print("Ошибка при выполнении запроса. Код ошибки:", response.status_code)
        return None


def get_full_info(access_token: str, page: int) -> str | None:
    """
    Функция для get запроса через API, получает информацию со
    всей страницы

    :param access_token: Токен доступа, получается после
    успешной авторизации и записывается в БД
    :param page: Номер страницы
    :return: Список страниц с нужной ифнормацией
    """
    url = "https://mc.dev.rand.agency/api/cabinet/individual-pages"

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json;charset=UTF-8",
        "Authorization": f"Bearer {access_token}"
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return pars_info(response.json()[page])

    else:
        print("Ошибка при выполнении запроса. Код ошибки:", response.status_code)
        return None

def get_full_info_as_js(access_token: str, page: int) -> str | None:
    """
    Функция для get запроса через API, получает информацию со
    всей страницы

    :param access_token: Токен доступа, получается после
    успешной авторизации и записывается в БД
    :param page: Номер страницы
    :return: Список страниц с нужной ифнормацией
    """
    url = "https://mc.dev.rand.agency/api/cabinet/individual-pages"

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json;charset=UTF-8",
        "Authorization": f"Bearer {access_token}"
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()[page]

    else:
        print("Ошибка при выполнении запроса. Код ошибки:", response.status_code)
        return None

def pars_info(jtext):
    result = "Основная информация:\n"
    result += f'Имя: {is_find(jtext, 'name')}\n'
    result += f'Фамилия: {is_find(jtext, 'surname')}\n'
    result += f'Отчество: {is_find(jtext, 'patronym')}\n'
    result += f'Дата рождения: {is_find(jtext, 'birthday_at')}\n'
    result += f'Дата Смерти: {is_find(jtext, 'died_at')}\n\n'
    result += f'Эпитафия: {is_find(jtext, 'epitaph')}\n'
    result += f'Автор: {is_find(jtext, 'author_epitaph')}\n\n'
    result += "Биография:\n"
    for bio in jtext['filled_fields']:
        result += bio + '\n'

    return result


def is_find(jtext, key):
    if jtext[key]:
        return jtext[key]
    else:
        return "Не заполнено"


def replace_user_texts(json_string, new_texts):
    data = json.loads(json_string)

    i = 0
    for message in data['messages']:
        if message['role'] == 'user':
            if i < len(new_texts):
                message['text'] = new_texts[i]
                i += 1

    return json.dumps(data, indent=4)


def get_json_string() -> str:
    # Пример использования:
    json_string = '''
    {
        "modelUri": "gpt://b1gu7e6h3d9j6nhp9nmt/yandexgpt-lite",
        "completionOptions": {
          "stream": false,
          "temperature": 0.6,
          "maxTokens": "2000"
        },
        "messages": [
          {
            "role": "system",
            "text": "На основе предоставленного контекста, создай хороший краткий текст одной эпитафии. В ответе напиши одну эпитафию. Не используй markdown."
          },
          {
            "role": "assistant",
            "text": "Как звали человека, о котором вы хотите создать страницу памяти?"
          },
          {
            "role": "user",
            "text": "Светлана"
          },
          {
            "role": "assistant",
            "text": "Что можно сказать о профессии или основном занятии человека?"
          },
          {
            "role": "user",
            "text": "Светлана была писателем, она внесла значительный вклад в культуру своего города."
          },
          {
            "role": "assistant",
            "text": "Какие достижения были у этого человека в его жизни? Какие награды он получал?"
          },
          {
            "role": "user",
            "text": "Больше всего в жизни Светлана ценила семью и дружбу. Она уделял много времени своим близким и всегда старалась поддерживать друзей в трудные моменты."
          }
        ]
    }
    '''

    return json_string
