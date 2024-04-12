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
