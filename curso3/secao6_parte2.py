# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# type: ignore

# O que é JSON - JavaScript Object Notation
# JSON - JavaScript Object Notation (extensão .json)
# É uma estrutura de dados que permite a serialização
# de objetos em texto simples para facilitar a transmissão de
# dados através da rede, APIs web ou outros meios de comunicação.
# O JSON suporta os seguintes tipos de dados:
# Números: podem ser inteiros ou com ponto flutuante, como 42 ou 3.14
# Strings: são cadeias de caracteres, como "Olá, mundo!" ou "12345"
#   As strings devem ser envolvidas por aspas duplas
# Booleanos: são os valores verdadeiro (true) ou falso (false)
# Arrays: são listas ordenadas de valores, como [1, 2, 3] ou
#   ["Oi", "Olá", "Bom dia"]
# Objetos: são conjuntos de pares chave/valor -> {"nome": "João", "idade": 30}
# null: é um valor especial que representa ausência de valor

# json.dumps e json.loads com strings + typing.TypedDict
# Ao converter de Python para JSON:
# Python        JSON
# dict          object
# list, tuple   array
# str           string
# int, float    number
# True          true
# False         false
# None          null

# import os
# import json
# from pprint import pprint
# from typing import \
#     TypedDict  # FAZ A TIPAGEM DE DICT UTILIZANDO UMA CLASSE HERDADA


# class Movie(TypedDict):
#     title: str
#     original_title: str
#     is_movie: bool
#     imdb_rating: float
#     year: int
#     characters: list[str]
#     budget: None | float


# string_json = '''
# {
#   "title": "O Senhor dos Anéis: A Sociedade do Anel",
#   "original_title": "The Lord of the Rings: The Fellowship of the Ring",
#   "is_movie": true,
#   "imdb_rating": 8.8,
#   "year": 2001,
#   "characters": ["Frodo", "Sam", "Gandalf", "Legolas", "Boromir"],
#   "budget": null
# }
# '''

# movie: Movie = json.loads(string_json)
# pprint(movie)
# print(movie["imdb_rating"])
# json_string = json.dumps(movie, ensure_ascii=False, indent=2)
# print(json_string)
# print(type(json_string), type(string_json))


# NOME_ARQUIVO = 'aula290.json'
# CAMINHO_ABSOLUTO_ARQUIVO = os.path.abspath(
#     os.path.join(
#         os.path.dirname(__file__),
#         NOME_ARQUIVO
#     )
# )

# string_json = '''
# {
#   "title": "O Senhor dos Anéis: A Sociedade do Anel",
#   "original_title": "The Lord of the Rings: The Fellowship of the Ring",
#   "is_movie": true,
#   "imdb_rating": 8.8,
#   "year": 2001,
#   "characters": ["Frodo", "Sam", "Gandalf", "Legolas", "Boromir"],
#   "budget": null
# }
# '''

# movie = json.loads(string_json)  # SALVANDO COMO DICIONÁRIO PYTHON

# movie = {
#     'title': 'O Senhor dos Anéis: A Sociedade do Anel',
#     'original_title': 'The Lord of the Rings: The Fellowship of the Ring',
#     'is_movie': True,
#     'imdb_rating': 8.8,
#     'year': 2001,
#     'characters': ['Frodo', 'Sam', 'Gandalf', 'Legolas', 'Boromir'],
#     'budget': None
# }

# with open(CAMINHO_ABSOLUTO_ARQUIVO, 'w') as arquivo:
#     json.dump(movie, arquivo, ensure_ascii=False, indent=2)

# with open(CAMINHO_ABSOLUTO_ARQUIVO, 'r') as arquivo:
#     filme_do_json = json.load(arquivo)
#     print(filme_do_json)

# import os
# from pathlib import Path

# import shutil
# PROJECT_PATH = Path()
# print(PROJECT_PATH)  # CAMINHO RELATIVO
# print(PROJECT_PATH.absolute())  # CAMINHO COMPLETO

# FILE_PATH = Path(__file__)  # CAMINHO DO ARQUIVO ATUAL
# PASTA DO ARQUIVO ATUAL - POSSIVEL CHAMAR MAIS .parent PARA IR ACIMA
# CRIANDO NOVO CAMINHO COM ADIÇÃO DE PASTAS E ARQUIVOS SEM REALMENTE CRIA
# new_folder = FILE_PATH.parent / 'new_file' / 'arquivo.txt'
# print(new_folder)

# HOME = Path.home()
# PROJECT_PATH = Path().absolute()
# NEW_PATH = PROJECT_PATH / 'new_file.txt'
# print(NEW_PATH)
# NEW_PATH.touch()  # CRIA ARQUIVOS (NÃO PASTAS)
# NEW_PATH.write_text('Olá mundo')  # ESCREVE NOS ARQUIVOS
# NEW_PATH.write_text('Olá mundo DE NOVO')  # FUNCIONA SOMENTE UMA VEZ
# print(NEW_PATH.read_text())  # LÊ O QUE ESTÁ ESCRITO NO ARQUIVO
# # NEW_PATH.unlink()  # APAGA ARQQUIVO
# with open(NEW_PATH, 'w') as file:
#     file.writelines('Olá mundo \nOlá mundo novamente')
#     file.writelines('\noutra linha \nmais uma linha')

# print(NEW_PATH.read_text())

# NEW_FOLDER = PROJECT_PATH / 'new_folder'
# NEW_FOLDER.mkdir(exist_ok=True)  # CRIA UM DIRETÓRIO
# SUB_FOLDER = NEW_FOLDER / 'sub-folder'
# SUB_FOLDER.mkdir(exist_ok=True)
# ANOTHER_FILE = SUB_FOLDER / 'another_file.txt'
# ANOTHER_FILE.touch()
# ANOTHER_FILE.write_text('Ola!')

# files = SUB_FOLDER / 'files'
# files.mkdir(exist_ok=True)

# for i in range(10):
#     file = files / f'file_{i}.txt'
#     # file.touch()
# if file.exists():
#     file.unlink()
# if file.exists():
#     file.write_text(f'oi - {i}')
# if file.is_file():
#     file.write_text(f'OLA - {i}')
# else:
#     file.touch()
# with file.open("a+") as text_file:
#     text_file.write(f"Olá Mundo - file_{i}")

# shutil.rmtree(caminho)


# def rmtree(root: Path, remove_root=True):
#     for file in root.glob('*'):
#         if file.is_dir():
#             print(f'DIR: {file}')
#             rmtree(file, False)
#             file.rmdir()
#         else:
#             print(f'FILE: {file}')
#             file.unlink()
#     if remove_root:
#         root.rmdir()

# CSV (Comma Separated Values - Valores separados por vírgulas)
# É um formato de arquivo que armazena dados em forma de tabela, onde cada
# linha representa uma linha da tabela e as colunas são separadas por vírgulas.
# Ele é amplamente utilizado para transferir dados entre sistemas de diferentes
# plataformas, como por exemplo, para importar ou exportar dados para uma
# planilha (Google Sheets, Excel, LibreOffice Calc) ou para uma base de dados.
# Um arquivo CSV geralmente tem a extensão ".csv" e pode ser aberto em um
# editor de texto ou em uma planilha eletrônica.
# Um exemplo de um arquivo CSV pode ser:
# Nome,Idade,Endereço
# Luiz Otávio,32,"Av Brasil, 21, Centro"
# João da Silva,55,"Rua 22, 44, Nova Era"
# A primeira linha do arquivo define os nomes das colunas, enquanto as
# linhas seguintes contêm os valores das linhas, separados por vírgulas.
# Regras simples do CSV
# 1 - Separe os valores das colunas com um delimitador único (,)
# 2 - Cada registro deve estar em uma linha
# 3 - Não deixar linhas ou espaços sobrando
# 4 - Use o caractere de escape (") quando o delimitador aparecer no valor.
# csv.reader e csv.DictReader
# csv.reader lê o CSV em formato de lista
# csv.DictReader lê o CSV em formato de dicionário
# import csv
# from pathlib import Path

# CAMINHO_CSV = Path(__file__).parent / 'aula293.csv'

# with open(CAMINHO_CSV, 'r') as arquivo:
#     # leitor = csv.reader(arquivo)  # formato lista
#     leitor = csv.DictReader(arquivo)  # formato dicionário
#     for linha in leitor:
#         print(linha, type(linha))


# csv.writer e csv.DictWriter para escrever em CSV
# csv.reader lê o CSV em formato de lista
# csv.DictReader lê o CSV em formato de dicionário

# import csv
# from pathlib import Path

# CAMINHO_CSV = Path(__file__).parent / 'aula294.csv'

# lista = [
#     {'Nome': 'Bruna Ballerini', 'Endereço': '"Rua Juscelino Barbosa - 86"'},
#     {'Nome': 'Marcelo Godde', 'Endereço': '"Rua Juscelino Barbosa - 86"'}
# ]
# COMO LISTA:
# with open(CAMINHO_CSV, 'w') as file:
#     chaves = lista[0].keys()
#     escritor = csv.writer(file)
#     escritor.writerow(chaves)
#     for i in range(len(lista)):
#         valores = lista[i].values()
#         escritor_valores = csv.writer(file)
#         escritor_valores.writerow(valores)

# print(lista[0].keys())
# for i in range(len(lista)):
#     valores = lista[i].values()
#     print(valores)

# COMO DICIONÁRIO:
# with open(CAMINHO_CSV, 'w') as file:
#     chaves = lista[0].keys()
#     escritor = csv.DictWriter(file, fieldnames=chaves)
#     escritor.writeheader()
#     print(chaves)
#     for pessoa in lista:
#         print(pessoa)
#         escritor_valores = csv.DictWriter(file, fieldnames=pessoa)
#         escritor_valores.writerow(pessoa)

# random tem geradores de números pseudoaleatórios
# Obs.: números pseudoaleatórios significa que os números
# parecem ser aleatórios, mas na verdade não são. Portanto,
# este módulo não deve ser usado para segurança ou uso criptográfico.
# O motivo disso é que quando temos uma mesma entrada e um mesmo algorítimo,
# a saída pode ser previsível.
# doc: https://docs.python.org/pt-br/3/library/random.html
# import random

# Funções:
# seed
#   -> Inicializa o gerador de random (por isso "números pseudoaleatórios")
# random.seed(0)  # import time ramdom.seed(time.time())

# random.randrange(início, fim, passo)
#   -> Gera um número inteiro aleatório dentro de um intervalo específico
# r_range = random.randrange(0, 100, 1)
# print(r_range)

# random.randint(início, fim)
#   -> Gera um número inteiro aleatório dentro de um intervalo "sem passo"
# r_int = random.randint(0, 200)
# print(r_int)

# random.uniform(início, fim)
#   -> Gera um número flutuante aleatório dentro de um intervalo "sem passo"
# r_uniform = random.uniform(0, 200)
# print(r_uniform)

# random.shuffle(SequenciaMutável) -> Embaralha a lista original
# nomes = ['Luiz', 'Maria', 'Helena', 'Joana']
# random.shuffle(nomes)
# print(nomes)

# random.sample(Iterável, k=N)
#   -> Escolhe elementos do iterável e retorna outro iterável (não repete)
# nomes = ['Luiz', 'Maria', 'Helena', 'Joana']
# novos_nomes = random.sample(nomes, k=3)
# print(nomes)
# print(novos_nomes)

# random.choices(Iterável, k=N)
#   -> Escolhe elementos do iterável e retorna outro iterável (repete valores)
# nomes = ['Luiz', 'Maria', 'Helena', 'Joana']
# novos_nomes = random.choices(nomes, k=3)
# print(nomes)
# print(novos_nomes)

# random.choice(Iterável) -> Escolhe um elemento do iterável
# print(random.choice(nomes))

# import secrets
# import string as s
# secrets gera números aleatórios seguros
# from secrets import SystemRandom as Sr

# random = secrets.SystemRandom()  # Sem importar o random -> seguro

# print(secrets.randbelow(100))
# print(secrets.choice([i for i in range(100)]))

# Criação de senhas aleatórias utilizando todos os caracteres de string
# print(''.join(Sr().choices(s.ascii_letters + s.digits + s.punctuation, k=5)))
# Comando para criação de senha no terminal
# python -c "import string as s;from secrets import SystemRandom as Sr;

# string.Template para substituir variáveis em textos
# doc: https://docs.python.org/3/library/string.html#template-strings
# Métodos:
# substitute: substitui mas gera erros se faltar chaves
# safe_substitute: substitui sem gerar erros
# Você também pode trocar o delimitador e outras coisas criando uma subclasse
# de template.
# import locale
# import string
# from datetime import datetime
# from pathlib import Path

# CAMINHO_ARQUIVO = Path(__file__).parent / 'aula298.txt'
# # print(CAMINHO_ARQUIVO)

# locale.setlocale(locale.LC_ALL, '')


# def converte_para_brl(numero: float) -> str:
#     brl = 'R$ ' + locale.currency(numero, symbol=False, grouping=True)
#     return brl


# data = datetime(2022, 12, 28)
# dados = dict(
#     nome='João',
#     valor=converte_para_brl(1_234_456),
#     data=data.strftime('%d/%m/%Y'),
#     empresa='O. M.',
#     telefone='+55 (11) 7890-5432'
# )
# Duas formas de impressão dos dados
# for chave, valor in dados.items():
#     print(f'{chave}: {valor}')
# import json
# print(json.dumps(dados, ensure_ascii=False,  indent=2))


# class MyTemplate(string.Template):  # delimitador padrão de string é $
#     delimiter = '%'


# with open(CAMINHO_ARQUIVO, 'r') as arquivo:
#     texto = arquivo.read()
#     template = MyTemplate(texto)  # template = string.Template(texto)
#     print(template.substitute(dados))
