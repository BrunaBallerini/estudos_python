# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=import-error

import requests
from fastapi import FastAPI, Query

app = FastAPI()


@app.get('/api/hello')
def hello():
    return {'hello': 'world'}


@app.get('/api/restaurants/')
def get_restaurant(restaurant: str = Query(None)):
    url = ('https://guilhermeonrails.github.io/api-restaurantes'
           '/restaurantes.json')
    response = requests.get(url)
    if response.status_code == 200:
        dados_json = response.json()
        if restaurant is None:
            return {'Dados': dados_json}

        dados_restaurante = []
        for item in dados_json:
            if item['Company'] == restaurant:
                dados_restaurante.append({
                    "item": item['Item'],
                    "price": item['price'],
                    "description": item['description']
                })
        return {'Restaurant': restaurant, 'Cardápio': dados_restaurante}
    return {'Erro': f'{response.status_code} - {response.text}'}
