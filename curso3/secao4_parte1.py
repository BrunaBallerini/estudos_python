# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# type: ignore


# def imprimir(a, b, c):
#     print(a, b, c)


# imprimir(b=2, a=5, c=3)

# nome = 'bruna fernandes ballerini'
# novo_nome = ''
# for letra in nome:
#     novo_nome += letra
# print(novo_nome)

# BEM INTERESSANTE!
# """
# Valores padrão para parâmetros
# Ao definir uma função, os parâmetros podem
# ter valores padrão. Caso o valor não seja
# enviado para o parâmetro, o valor padrão será
# usado.
# Refatorar: editar o seu código.
# """
# def soma(x, y, z=None):
#     if z is not None:
#         print(f'{x=} {y=} {z=}', x + y + z)
#     else:
#         print(f'{x=} {y=}', x + y)
# soma(1, 2)
# soma(3, 5)
# soma(100, 200)
# soma(7, 9, 0)
# soma(y=9, z=0, x=7)

# def multiplica(*args):
#     total = 1
#     # print(args) # empacotamento em tupla
#     for numero in args:
#         total *= numero
#     return total

# valor = multiplica(1, 2, 3, 4, 5)
# print(valor)

# def par_impar(numero):
#     if numero % 2 == 0:
#         return f'{numero}: PAR'
#     return f'{numero}: IMPAR'

# print(par_impar(15))

# def par_impar(*args):
#     for numero in args:
#         print (f'{numero}: P') if numero % 2 == 0 else print(f'{numero}: I')

# par_impar(1, 2, 3, 4, 5)

# def par_impar(*args):
#     lista = []
#     for numero in args:
#         if numero % 2 == 0:
#             lista.append(f'{numero}: PAR')
#         else:
#             lista.append(f'{numero}: IMPAR')
#     return lista

# print(par_impar(1, 2, 3, 4, 5))

# def criar_multiplicador(multiplicador):
#     def multiplicar (numero):
#         return numero * multiplicador
#     return multiplicar

# quadruplo = criar_multiplicador(4)
# print(quadruplo(2))
# quintuplo = criar_multiplicador(5)
# print(quintuplo(10))

# def saudacao(saudacao):
#     def saudar(nome):
#         return f'{saudacao}, {nome}'
#     return saudar

# bom_dia = saudacao('Bom dia')
# print(bom_dia('Luiz'))
# print(bom_dia('Maria'))

# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro
# pessoa = {
#     'nome': 'Luiz Otávio',
#     'sobrenome': 'Miranda',
#     'idade': 18,
#     'altura': 1.8,
#     'enderecos': [
#         {'rua': 'primeira rua', 'número': 123},
#         {'rua': 'segunda rua', 'número': 321},
#     ],
# }
# print(pessoa['enderecos'][0]['rua'])
# pessoa['celular'] = 999999999
# del pessoa['sobrenome']
# if pessoa.get('sobrenome') is None:
#     print('Não existe')
# else:
#     print(pessoa['sobrenome'])
# pessoa.setdefault('escolaridade', None)
# print(pessoa['idade'])
# for chave, valor in pessoa.items():
#     print(chave, valor)
# for chave in pessoa:
#     print(chave, pessoa[chave])

# perguntas = [
#     {
#         'Pergunta': 'Quanto é 2+2?',
#         'Opções': ['1', '3', '4', '5'],
#         'Resposta': '4',
#     },
#     {
#         'Pergunta': 'Quanto é 5*5?',
#         'Opções': ['25', '55', '10', '51'],
#         'Resposta': '25',
#     },
#     {
#         'Pergunta': 'Quanto é 10/2?',
#         'Opções': ['4', '5', '2', '1'],
#         'Resposta': '5',
#     },
# ]
# MINHA RESOLUÇÃO:
# for pergunta in perguntas:
#     print(f'Pergunta: {pergunta.get("Pergunta")}')
#     print(f'Opções:\n')
#     for index, opcao in enumerate(pergunta["Opções"]):
#         print (f'{index}) {opcao}')
#     chute = input('Dentre as opções digite sua resposta: ')
#     if chute == pergunta["Resposta"]:
#         print('Acertou!\n')
#     else:
#         print('Errou!\n')

# RESOLUÇÃO PROFESSOR:
# contador_acertos = 0
# for pergunta in perguntas:
#     print(f'Pergunta: {pergunta.get("Pergunta")}\n')
#     print(f'Opções:')

#     opcoes = pergunta["Opções"]
#     qtd_pergunta = len(pergunta)
#     for index, opcao in enumerate(opcoes):
#         print (f'{index}) {opcao}')

#     chute = input('Digite o indice da sua resposta: ')
#     chute_int = None
#     acertou = False

#     if chute.isdigit():
#         chute_int = int(chute)
#     if chute_int is not None:
#         if 0 <= chute_int <= qtd_pergunta:
#             if opcoes[chute_int] == pergunta['Resposta']:
#                 acertou = True
#     if acertou:
#         print('\nAcertou!\n')
#         contador_acertos += 1
#     else:
#         print('\nErrou!\n')
# print(f'Acertos {contador_acertos}')

# """
# Exercício
# Crie uma função que encontra o primeiro duplicado considerando o segundo
# número como a duplicação. Retorne a duplicação considerada.
# Requisitos:
#     A ordem do número duplicado é considerada a partir da segunda
#     ocorrência do número, ou seja, o número duplicado em si.
#     Exemplo:
#         [1, 2, 3, ->3<-, 2, 1] -> 1, 2 e 3 são duplicados (retorne 3)
#         [1, 2, 3, 4, 5, 6] -> Retorne -1 (não tem duplicados)
#         [1, 4, 9, 8, ->9<-, 4, 8] (retorne 9)
#     Se não encontrar duplicados na lista, retorne -1
# """
# lista_de_listas_de_inteiros = [
#     [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
#     [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
#     [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
#     [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
#     [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
#     [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
#     [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
#     [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
#     [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
#     [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
#     [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
#     [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
# ]


# def numeros_duplicados(lista):
#     set1 = set(lista)
#     print(set1)

# DESENVOLVIMENTO 1
# set1 = {9, 1, 8, 9, 9, 7, 2, 1, 6, 8}
# numeros = [1, 3, 2, 2, 8, 6, 5, 9, 6, 7]
# set_novo = set()
# comparador = 0
# for comparador in range(11):
#     if comparador == set1:
#         set_novo.add(comparador)
#         comparador += 1
# print(set_novo)

# DESENVOLVIMENTO 2:
# numeros = [1, 3, 2, 2, 8, 2]
# comparador = 0
# qtas_vezes = 0
# numeros_repetidos = {}
# for n in numeros:
#     if n == comparador:
#         qtas_vezes += 1
#         numeros_repetidos.update({n: qtas_vezes})
#         print(n, qtas_vezes)
#     else:
#         comparador = n
# print(numeros_repetidos)

# PRIMEIRA RESOLUÇÃO
# def repetidos(lista_de_listas_de_inteiros):
#     numeros_repetidos = {}
#     for lista in lista_de_listas_de_inteiros:
#         for n in lista:
#             if n in numeros_repetidos:
#                 numeros_repetidos[n] += 1
#             else:
#                 numeros_repetidos[n] = 1
#     # print(numeros_repetidos)

#     mais_vezes = 0
#     for chave, valor in numeros_repetidos.items():
#         if valor > mais_vezes:
#             mais_vezes  = valor
#             chave_maior = chave
#     # print(mais_vezes, chave_maior)
#     return f'Número: {chave_maior} - {mais_vezes} vezes'

# print(
#     repetidos(
#         lista_de_listas_de_inteiros = [
#     [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
#     [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
#     [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
#     [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
#     [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
#     [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
#     [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
#     [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
#     [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
#     [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
#     [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
#     [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
#         ]
#     )
# )

# """
# Exercício
# Crie uma função que encontra o primeiro duplicado considerando o segundo
# número como a duplicação. Retorne a duplicação considerada.
# Requisitos:
#     A ordem do número duplicado é considerada a partir da segunda
#     ocorrência do número, ou seja, o número duplicado em si.
#     Exemplo:
#         [1, 2, 3, ->3<-, 2, 1] -> 1, 2 e 3 são duplicados (retorne 3)
#         [1, 2, 3, 4, 5, 6] -> Retorne -1 (não tem duplicados)
#         [1, 4, 9, 8, ->9<-, 4, 8] (retorne 9)
#     Se não encontrar duplicados na lista, retorne -1
# """
# lista_de_listas_de_inteiros = [
#     [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
#     [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
#     [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
#     [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
#     [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
#     [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
#     [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
#     [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
#     [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
#     [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
#     [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
#     [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
# ]

# def encontra_primeiro_duplicado(lista_de_inteiros):
#     numeros_checados = set()
#     primeiro_duplicado = -1
#     for numero in lista_de_inteiros:
#         if numero in numeros_checados:
#             primeiro_duplicado = numero
#             break
#         numeros_checados.add(numero)
#     return primeiro_duplicado

# for lista in lista_de_listas_de_inteiros:
#     print(
#         lista,
#         encontra_primeiro_duplicado(lista)
#     )

# lista_de_listas_de_inteiros = [
#     [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
#     [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
#     [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
#     [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
#     [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
#     [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
#     [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
#     [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
#     [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
#     [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
#     [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
#     [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
# ]

# def repetidos(lista):
#     numeros_checados = set()
#     duplicacao = -1
#     for n in lista:
#         if n in numeros_checados:
#             duplicacao = n
#             return duplicacao
#         else:
#             numeros_checados.add(n)
#     return duplicacao

# for lista in lista_de_listas_de_inteiros:
#     print(lista, repetidos(lista))
