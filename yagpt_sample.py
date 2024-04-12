import requests
import json
import os

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

if __name__ == "__main__":
    with open('credentials.json', 'r') as f:
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
        print ('Please save either an IAM token or an API key into a corresponding `IAM_TOKEN` or `API_KEY` environment variable.')
        exit()

    print(gpt(headers))
