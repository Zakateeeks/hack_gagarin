import requests


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


def pars_info(jtext):
    result = "Основная информация:\n"
    result += f'Имя: {is_find(jtext, 'name')}\n'
    result += f'Фамилия: {is_find(jtext, 'surname')}\n'
    result += f'Отчество: {is_find(jtext, 'patronym')}\n'
    result += f'Дата рождения: {is_find(jtext, 'birthday_at')}\n'
    result += f'Дата рождения: {is_find(jtext, 'died_at')}\n\n'
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


print(get_full_info('2631|xCCLQ2OlGZYTLvxAHbrHISfIzljP4hnOLU2bz9aL', 0))
