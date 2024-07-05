from pprint import pprint

import requests
from get_token import token

_print = pprint
print = pprint

url = 'http://127.0.0.1:3001/alunos'

headers = {
    'Authorization': token
}

aluno_data = {
    "nome": "Luana",
    "sobrenome": "Silva",
    "email": "luana@email.com",
    "idade": "34",
    "peso": "101.04",
    "altura": "1.70"
}

response = requests.post(url=url, json=aluno_data, headers=headers)

if response.status_code >= 200 and response.status_code <= 299:
    print(response.status_code)
    print(response.reason)
    print(response.text)
    print(response.json())
else:
    print(response.status_code)
    print(response.reason)
    print(response.text)
