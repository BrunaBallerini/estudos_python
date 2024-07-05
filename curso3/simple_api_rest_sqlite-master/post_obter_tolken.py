from pprint import pprint

import requests

_print = pprint

url = 'http://127.0.0.1:3001/tokens'

user_data = {
    "email": "admin@email.com",
    "password": "123456"
}

response = requests.post(url=url, json=user_data)

if response.status_code >= 200 and response.status_code <= 299:
    print(response.status_code)
    print(response.reason)
    print(response.text)
    response_data = response.json()
    token = response_data['token']

    with open('token.txt', 'w') as file:
        file.write(token)

else:
    print(response.status_code)
    print(response.reason)
    print(response.text)
