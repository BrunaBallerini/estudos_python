# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=no-name-in-module
# pylint: disable=import-error
# pylint: disable=unused-import
# flake8: disable=F401
# type:ignore

import json
import pathlib

import requests

caminho = pathlib.Path(__file__).parent / 'dados'

# dados_restaurante = {
#     'McDonald's': [
#         {'item': 'xxx', 'price': yyy, 'description': 'zzz'},
#         {'item': 'xxx', 'price': yyy, 'description': 'zzz'},
#     ],
# }

URL = ('https://guilhermeonrails.github.io/api-restaurantes/'
       'restaurantes.json')
response = requests.get(URL)
# print(response.status_code)
if response.status_code == 200:
    dados_json = response.json()
    print(type(dados_json))
    dados_restaurante = {}
    for item in dados_json:
        nome_restaurante = item['Company']
        if nome_restaurante not in dados_restaurante:
            dados_restaurante[nome_restaurante] = []
        dados_restaurante[nome_restaurante].append({
            "item": item['Item'],
            "price": item['price'],
            "description": item['description']
        })
    # FORMA DE IMPRIMIR:
    for nome_restaurante, dados in dados_restaurante.items():
        print(nome_restaurante)
        for dado in dados:
            print(dado)
    for nome_restaurante, dados in dados_restaurante.items():
        nome_arquivo = f'{caminho}/{nome_restaurante}.json'
        with open(nome_arquivo, 'w', encoding='utf8') as arquivo_restaurante:
            json.dump(dados, arquivo_restaurante, indent=4, ensure_ascii=False)
else:
    print(f'O erro foi {response.status_code}')

URL = "https://economia.awesomeapi.com.br/last/USD-BRL"
response = requests.get(URL)

if response.status_code == 200:
    data = response.json()
    cotacao = float(data['USDBRL']['bid'])
    mensagem = f"U$ 1 dólar corresponde a R$ {cotacao:.2f}"
    print(mensagem)
    for keys, values in data.items():
        print(keys)
        print()
        for key, value in values.items():
            print(f'{key} - {value}')
else:
    print(f"A requisição falhou com o código de status {response.status_code}")
