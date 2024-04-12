import requests


def authentication(email: str, password: str) -> str:
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
        return response.text
