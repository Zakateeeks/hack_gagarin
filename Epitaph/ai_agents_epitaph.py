import requests
import json
import os
import time

def gpt(auth_headers):
    url = 'https://llm.api.cloud.yandex.net/foundationModels/v1/completion'

    with open('body.json', 'r', encoding='utf-8') as f:
        data = json.dumps(json.load(f))
    resp = requests.post(url, headers=auth_headers, data=data)

    if resp.status_code != 200:
        raise RuntimeError(
            'Invalid response received: code: {}, message: {}'.format(
                {resp.status_code}, {resp.text}
            )
        )

    return resp.text


def analyzerAgentGpt(auth_headers, prev_result):
    # Преобразуем строку prev_result в JSON объект
    prev_result_json = json.loads(prev_result)
    # Извлекаем текст ответа
    analyzer_text = prev_result_json['result']['alternatives'][0]['message']['text']

    # Загружаем содержимое bodyAnalyzer.json
    with open('bodyAnalyzer.json', 'r', encoding='utf-8') as f:
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

def rewriterAgentGpt(auth_headers, prev_result):
    # Преобразуем строку prev_result в JSON объект
    prev_result_json = json.loads(prev_result)
    # Извлекаем текст ответа
    analyzer_text = prev_result_json['result']['alternatives'][0]['message']['text']

    # Загружаем содержимое bodyRewriter.json
    with open('bodyRewriter.json', 'r', encoding='utf-8') as f:
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


if __name__ == "__main__":
    with open('../credentials.json', 'r') as f:
        data = json.load(f)
    if data.get('IAM_TOKEN') is not None:
        print("IAM_TOKEN was found")
        iam_token = data['IAM_TOKEN']
        headers = {
            'Authorization': f'Bearer {iam_token}',
        }
    elif data.get('API_KEY') is not None:
        print("API_KEY was found")
        api_key = data['API_KEY']
        headers = {
            'Authorization': f'Api-Key {api_key}',
        }
    else:
        print(
            'Please save either an IAM token or an API key into a corresponding `IAM_TOKEN` or `API_KEY` environment variable.')
        exit()

    firts_epitafia = gpt(headers)
    print(firts_epitafia)

    time.sleep(0.5)
    print('\n')
    result = analyzerAgentGpt(headers, firts_epitafia)
    print(result)

    # Преобразуем строку prev_result в JSON объект
    result_json = json.loads(result)
    # Извлекаем текст ответа
    text = result_json['result']['alternatives'][0]['message']['text']

    print(len(text))

    if len(text) > 300:
        time.sleep(0.5)
        a = rewriterAgentGpt(headers, result)
        print(a)
        new_json = json.loads(a)
        new_text = new_json['result']['alternatives'][0]['message']['text']
        print(len(new_text))
