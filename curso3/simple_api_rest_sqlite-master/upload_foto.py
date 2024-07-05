from mimetypes import MimeTypes
from pprint import pprint

import requests
from get_token import token
from requests_toolbelt import MultipartEncoder

_print = pprint
print = pprint

mimetypes = MimeTypes()

caminho_arquivo = 'pyhton_logo.png'

mimetype_arquivo = mimetypes.guess_type(caminho_arquivo)[0]

multipart = MultipartEncoder(fields={
    'aluno_id': '2',
    'foto': (caminho_arquivo, open(caminho_arquivo, 'rb'), mimetype_arquivo)
})


url = 'http://127.0.0.1:3001/fotos'

headers = {
    'Authorization': token,
    'Content-Type': multipart.content_type
}

response = requests.post(url=url, headers=headers)

if response.status_code >= 200 and response.status_code <= 299:
    print(response.status_code)
    print(response.reason)
    print(response.text)
    print(response.json())
else:
    print(response.status_code)
    print(response.reason)
    print(response.text)
