import requests
import json
import os
import time


def gpt(data):
    url = 'https://llm.api.cloud.yandex.net/foundationModels/v1/completion'

    auth_headers = create_auth_headers()
    resp = requests.post(url, headers=auth_headers, data=data)

    if resp.status_code != 200:
        raise RuntimeError(
            'Invalid response received: code: {}, message: {}'.format(
                {resp.status_code}, {resp.text}
            )
        )

    return resp.text


def analyzerAgentGpt(prev_result):
    auth_headers = create_auth_headers()
    # Преобразуем строку prev_result в JSON объект
    prev_result_json = json.loads(prev_result)
    # Извлекаем текст ответа
    analyzer_text = prev_result_json['result']['alternatives'][0]['message']['text']

    # Загружаем содержимое bodyAnalyzer.json
    with open('../Epitaph/bodyAnalyzer.json', 'r', encoding='utf-8') as f:
        body_data = json.load(f)

    # Добавляем текст из analyzerAgentGpt в messages bodyAnalyzer.json
    user_message = {
        "role": "user",
        "text": analyzer_text
    }
    body_data['messages'].append(user_message)

    # Конвертируем обновлённый body_data обратно в строку для отправки
    data = json.dumps(body_data)

    # Отправляем запрос
    url = 'https://llm.api.cloud.yandex.net/foundationModels/v1/completion'
    resp = requests.post(url, headers=auth_headers, data=data)

    if resp.status_code != 200:
        raise RuntimeError(
            'Invalid response received: code: {}, message: {}'.format(
                resp.status_code, resp.text
            )
        )

    return resp.text


def rewriterAgentGpt(prev_result):
    # Преобразуем строку prev_result в JSON объект
    prev_result_json = json.loads(prev_result)
    auth_headers = create_auth_headers()
    # Извлекаем текст ответа
    analyzer_text = prev_result_json['result']['alternatives'][0]['message']['text']

    # Загружаем содержимое bodyRewriter.json
    with open('../Epitaph/bodyRewriter.json', 'r', encoding='utf-8') as f:
        body_data = json.load(f)

    # Добавляем текст в messages bodyRewriter.json
    user_message = {
        "role": "user",
        "text": analyzer_text
    }
    body_data['messages'].append(user_message)

    # Конвертируем обновлённый body_data обратно в строку для отправки
    data = json.dumps(body_data)

    # Отправляем запрос
    url = 'https://llm.api.cloud.yandex.net/foundationModels/v1/completion'
    resp = requests.post(url, headers=auth_headers, data=data)

    if resp.status_code != 200:
        raise RuntimeError(
            'Invalid response received: code: {}, message: {}'.format(
                resp.status_code, resp.text
            )
        )

    return resp.text


def create_auth_headers():
    with open('../credentials.json', 'r') as f:
        data = json.load(f)
    if data.get('IAM_TOKEN') is not None:
        print("IAM_TOKEN was found")
        iam_token = data['IAM_TOKEN']
        folder_id = data["FOLDER_ID"]
        headers = {
            'Authorization': f'Bearer {iam_token}',
            "x-folder-id": f"{folder_id}",
        }
    elif data.get('API_KEY') is not None:
        print("API_KEY was found")
        api_key = data['API_KEY']
        folder_id = data["FOLDER_ID"]
        headers = {
            'Authorization': f'Api-Key {api_key}',
            "x-folder-id": f"{folder_id}",
        }
    else:
        print(
            'Please save either an IAM token or an API key into a corresponding IAM_TOKEN or API_KEY environment variable.')
        exit()

    return headers
