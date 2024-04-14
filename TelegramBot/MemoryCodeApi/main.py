import requests
from TelegramBot.MemoryCodeApi import personal_info


def authentication(email: str, password: str) -> str:
    """
    Аутинификация с помощью API на сайте Код Памяти

    :param email: почта-логин пользователя
    :param password: пароль пользователя
    :return: Токен какой-то
    """

    URL = "https://mc.dev.rand.agency/api/v1/get-access-token"

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json;charset=UTF-8"
    }
    payload = {
        "email": email,
        "password": password,
        "device": "bot-v0.0.1"
    }

    response = requests.post(URL, json=payload, headers=headers)

    if response.status_code == 200:
        access_token = response.json()["access_token"]
        print("Авторизация прошла успешно.")
        return access_token
    else:
        # Обработка ошибок
        print("Ошибка при авторизации. Код ошибки:", response.status_code)
        return None


def fill_data(epitaph: str, token: str, page: int):
    js = personal_info.get_full_info_as_js(token, page)

    URL = js['link'].replace("\\", "")

    js['epitaph'] = epitaph

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json;charset=UTF-8",
        "Authorization": f"Bearer {token}"
    }

    response = requests.post(URL, json=js, headers=headers)
    if response.status_code == 200:
        print("Авторизация прошла успешно.")
        return response
    else:
        # Обработка ошибок
        print("Ошибка при авторизации. Код ошибки:", response.status_code)
        return None
