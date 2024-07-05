# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# type: ignore

# EMPACOTAMENTO E DESEMPACOTAMENTO DE DICIONÁRIOS (**)
# DESEMPACOTAMENTO DE LISTAS (*)

# a, b = 1, 2
# a, b = b, a
# pessoa = {
#     'nome': 'Aline',
#     'sobrenome': 'Souza',
# }
# dados_pessoa = {
#     'idade': 16,
#     'altura': 1.6,
# }
# (a1, a2), (b1, b2) = pessoa.items()
# print(a1, a2)
# print(b1, b2)
# for chave, valor in pessoa.items():
#     print(chave, valor)
# pessoas_completa = {**pessoa, **dados_pessoa, 'outra_chave': 'outro_valor'}
# for chave, valor in pessoas_completa.items():
#     print(chave, valor)
# print(pessoas_completa)
# print(pessoa)

# args e kwargs
# kwargs - keyword arguments (argumentos nomeados)
# def mostro_argumentos_nomeados(*args, **kwargs):
#     print('NÃO NOMEADOS:', args)
#     for chave, valor in kwargs.items():
#         print(chave, valor)
# mostro_argumentos_nomeados(nome='Joana', qlq=123)
# mostro_argumentos_nomeados(**pessoas_completa)

# MAPEAMENTO DE DADOS
# produtos = [
#     {'nome': 'p1', 'preco': 20, },
#     {'nome': 'p2', 'preco': 10, },
#     {'nome': 'p3', 'preco': 30, },
# ]
# novos_produtos = []
# for produto in produtos:
#     novos_produtos.append({**produto})
# print(*novos_produtos, sep='\n')

# FORMA QUE NÃO RETORNOU O DICIONÁRIO CORRETAMENTE:
# # novos_produtos = []
# # for produto in produtos:
# #     for chave, valor in produto.items():
# #         novos_produtos.append({chave: valor})
# # print(novos_produtos)
# # print(*novos_produtos, sep='\n')

# MAPEAMENTO DE DADOS COM ALTERAÇÕES
# produtos = [
#     {'nome': 'p1', 'preco': 20, },
#     {'nome': 'p2', 'preco': 10, },
#     {'nome': 'p3', 'preco': 30, },
# ]
# novos_produtos = []
# for produto in produtos:
#     novos_produtos.append({**produto, 'preco': produto['preco'] * 1.05})
# print(*novos_produtos, sep='\n')

# produtos = [
#     {'nome': 'p1', 'preco': 20, },
#     {'nome': 'p2', 'preco': 25, },
#     {'nome': 'p3', 'preco': 30, },
# ]
# novos_produtos = []
# for produto in produtos:
#     if produto['preco'] > 20:
#         novos_produtos.append({**produto, 'preco': produto['preco'] * 1.05})
#     else:
#         novos_produtos.append({**produto})
# print(*novos_produtos, sep='\n')
# *args -> IMPRIMI TODOS DENTRO DA LISTA SEPARANDO POR \n

# LIST COMPREHENSION É UMA FORMA RÁPIDA DE CIRAR LISTAS A PARTIR DE ITERÁVEIS
# print(list(range(10)))
# lista = []
# for numero in range(10):
#     lista.append(numero)
# lista = [
#     numero * 2
#     for numero in range(10)
# ]

# MAPEAMENTO DE DADOS EM LIST COMPREHENSION
# produtos = [
#     {'nome': 'p1', 'preco': 20, },
#     {'nome': 'p2', 'preco': 10, },
#     {'nome': 'p3', 'preco': 30, },
# ]
# novos_produtos = [
#     {**produto, 'preco': produto['preco'] * 1.05}
#     if produto['preco'] > 20 else {**produto}
#     for produto in produtos
# ]
# print(novos_produtos)
# print(*novos_produtos, sep='\n')
# Operação ternária (condicional de uma linha)
# <valor> if <condicao> else <outro valor>

# MAPEAMENTO DE DADOS EM LIST COMPREHENSION E FILTER
# import pprint
# def p(v):
#     pprint.pprint(v, sort_dicts=False, width=40)
# produtos = [
#     {'nome': 'p1', 'preco': 20, },
#     {'nome': 'p2', 'preco': 10, },
#     {'nome': 'p3', 'preco': 30, },
# ]
# novos_produtos = [
#     {**produto, 'preco': produto['preco'] * 1.05}
#     if produto['preco'] > 20 else {**produto}
#     for produto in produtos
#     if (produto['preco'] >= 20 and produto['preco'] * 1.05) > 10
# ]
# p(novos_produtos)

# RETIRANDO LIST COMPREHENSION
# produtos = [
#     {'nome': 'p1', 'preco': 20, },
#     {'nome': 'p2', 'preco': 10, },
#     {'nome': 'p3', 'preco': 30, },
# ]
# novos_produtos = []
# for produto in produtos:
#     if produto['preco'] >= 20 and produto['preco'] * 1.05 > 10:
#         if produto['preco'] > 20:
#             novos_produtos.append({**produto,
#                       'preco': produto['preco'] * 1.05})
#         else:
#             novos_produtos.append({**produto})
# print(novos_produtos)

# MANIPULAÇÃO DE STRING
# string = 'BrunaBallerini'
# numero_letras = 2
# nova_string = '.'.join([string[indice: indice + numero_letras]
#                          for indice in range(0, len(string), numero_letras)])
# print(nova_string)

# nomes = ['bruna', 'maria', 'marcelo', 'joana']
# novos_nomes = [f'{nome[:-1].lower()}{nome[-1].upper()}' for nome in nomes]
# print(novos_nomes)

# DICTIONARY E SET COMPREHENSION
# produto = {
#     'nome': 'Caneta Azul',
#     'preco': 2.5,
#     'categoria': 'Escritório',
# }
# dc = {
#     chave: valor.upper()
#     VERIFICA SE VALOR É UMA STRING, SE FOR CONDIÇÃO ACIMA, SENÃO ELSE
#     if isinstance(valor, str) else valor
#     for chave, valor in produto.items()
#     if chave != 'categoria' # FILTRO -> SE CHAVE == CATEGORIA NÃO INCLUI
# }
# print(dc)
# dc = {}
# for chave, valor in produto.items():
#     if chave != 'categoria':
#         if isinstance(valor, str):
#             dc[chave] = valor.upper()
#         else:
#             dc[chave] = valor
# print(dc)
# lista = [
#     ('a', 'valor a'),
#     ('b', 'valor b'),
#     ('b', 'valor c'),
# ]
# dc = {
#     chave: valor
#     for chave, valor in lista
# }
# s1 = {2 ** i for i in range(10)}
# print(s1)
# s2 = set()
# for i in range(10):
#     valor = 2 ** i
#     s2.add(valor)
# print(s2)
# isinstace - VERIFICA TIPO DO OBJETO
# lista = [
#      TRUE/FALSE -> SUBTIPO DE INT -> TRUE É 1, FALSE É 0
#     'a', 1, 1.1, [0, 1, 2], (1, 2),
#     {0, 1}, True, {'nome': 'Luiz'},
# ]
# for item in lista:
#     if isinstance(item, set):
#         print('SET')
#         item.add(5)
#         print(item, isinstance(item, set))
#     elif isinstance(item, str):
#         print('STR')
#         print(item.upper())
#     elif isinstance(item, (int, float)):
#         print('NUM')
#         print(item, item * 2)
#     else:
#         print('OUTRO')
#         print(item)

# MUTÁVIES [] {} set()
# IMUTÁVEIS () "" 0 0.0 None False range(0, 10)
# lista = []
# dicionario = {}
# conjunto = set()
# tupla = ()
# string = ''
# inteito = 0
# flutuante = 0.0
# nada = None
# falso = False
# intervalo = range(0)
# def falsy(valor):
#     return 'falsy'if not valor else 'truthy'
# print(f'TESTE', falsy('TESTE'))
# print(f'{lista=}', falsy(lista))
# print(f'{dicionario=}', falsy(dicionario))
# print(f'{conjunto=}', falsy(conjunto))
# print(f'{tupla=}', falsy(tupla))
# print(f'{string=}', falsy(string))
# print(f'{inteito=}', falsy(inteito))
# print(f'{flutuante=}', falsy(flutuante))
# print(f'{nada=}', falsy(nada))
# print(f'{falso=}', falsy(falso))
# print(f'{intervalo=}', falsy(intervalo))

# dir, hasattr e getattr em Python
# string = '     Luiz     '
# metodo = 'strip'
# if hasattr(string, metodo):
#     print(getattr(string, metodo)())
# else:
#     print('Não existe o método', metodo)

# print('Este módulo se chama', __name__)
# variavel_modulo = 'Bruna'
