from pprint import pprint

import requests

_print = pprint
print = pprint

url = 'http://127.0.0.1:3001/users'

user_data = {
    "nome": "Bruna Fernandes",
    "password": "123456",
    "email": "brunafb@email.com"
}

response = requests.post(url=url, json=user_data)

if response.status_code >= 200 and response.status_code <= 299:
    print(response.status_code)
    print(response.reason)
    print(response.text)
    print(response.json())
else:
    print(response.status_code)
    print(response.reason)
    print(response.text)
