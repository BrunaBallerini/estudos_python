# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# type: ignore

# # COUNT -> ITERATOR SEM FIM
# from itertools import count
# c1 = count(step=8, start=8)
# r1 = range(8, 100, 8)
# print('c1', hasattr(c1, '__iter__')) # ITERÁVEL
# print('c1', hasattr(c1, '__next__')) # ITERATOR -> COUNT É UM ITERATOR
# print('r1', hasattr(r1, '__iter__')) # ITERÁVEL
# print('r1', hasattr(r1, '__next__')) # NÃO É ITERATOR -> RANGE É UM ITERÁVEL

# print('count')
# for i in c1:
#     if i >= 100: # NÃO TEM FIM, PRECISA DE UM BREAK
#         break
#     print(i)
# print()
# print('range')
# for i in r1:
#     print(i)

# COMBINATIONS - Ordem não importa - iterável + tamanho do grupo
# PERMUTATIONS - Ordem importa
# PRODUTC - Ordem importa e repete valores únicos
# from itertools import combinations, permutations, product
# def print_iter(iterator):
#     print(*list(iterator), sep='\n')
#     print()
# pessoas = [
#     'João', 'Joana', 'Luiz', 'Letícia',
# ]
# camisetas = [
#     ['preta', 'branca'],
#     ['p', 'm', 'g'],
#     ['masculino', 'feminino', 'unisex'],
#     ['algodão', 'poliéster']
# ]
# # print_iter(combinations(pessoas, 2))
# # print_iter(permutations(pessoas, 2))
# print_iter(product(pessoas, repeat= 2)) # * DESEMPACOTA A LISTA

# # GROUPBY - AGRUPANDO VALORES
# import copy
# from itertools import groupby
# alunos = [
#     {'nome': 'Luiz', 'nota': 'A'},
#     {'nome': 'Letícia', 'nota': 'B'},
#     {'nome': 'Fabrício', 'nota': 'A'},
#     {'nome': 'Rosemary', 'nota': 'C'},
#     {'nome': 'Joana', 'nota': 'D'},
#     {'nome': 'João', 'nota': 'A'},
#     {'nome': 'Eduardo', 'nota': 'B'},
#     {'nome': 'André', 'nota': 'A'},
#     {'nome': 'Anderson', 'nota': 'C'},
# ]
# def ordem_sort_nota(dicionario):
#   return dicionario['nota']
# # CRIAÇÃO DA FUNÇÃO POR LAMBDA
# # lambda dicionario: dicionario["nota"]
# # CRIA DICIONÁRIO -> MESMO EFEITO DA DEEPCOPY
# # alunos_copia_2 = [
# #    {**aluno}
# #    for aluno in alunos
# # ]
# # print(*alunos_copia_2, sep='\n')
# # print()
# alunos_copia = copy.deepcopy(alunos)
# USEI A SORTED PARA SALVAR EM OUTRA LISTA
# # alunos_copia_ordenada.sort(reverse=False, key=ordem_sort_nota)
# alunos_ordenados = sorted(alunos_copia, key= ordem_sort_nota)
# print(*alunos_ordenados, sep='\n')
# print()
# alunos_agrupados = groupby(alunos_ordenados, key= ordem_sort_nota)
# for chave, grupo in alunos_agrupados:
#   print(chave, list(grupo))

# MAP, PARTIAL
# from functools import partial
# from dados import produtos
# def imprimir(iteravel):
#     print(*iteravel, sep='\n')
# def aumenta_preco(valor, porcentagem):
#     return round((valor * porcentagem), 2)
# # CLOUSURE
# # def cria_funcao(funcao, x):
# #     def interna(y):
# #         return funcao(x, y)
# #     return interna
# # aumenta_dez_porcento = cria_funcao(aumenta_preco, 1.10)
# # PARTIAL
# aumenta_dez_porcento = partial(aumenta_preco, 1.10)
# # MAPEAMENTO CRIANDO LISTAS NOVAS
# # novos_produtos = [
# #     {**produto, 'preco': aumenta_dez_porcento(produto['preco'])}
# #     for produto in produtos
# # ]
# #MAPEAMENTO UTILIZANDO MAP
# def muda_preco_produtos(produto):
#     return {**produto, 'preco': aumenta_dez_porcento(produto['preco'])}
# novos_produtos = list(map(
#     muda_preco_produtos, produtos
# ))
# imprimir(novos_produtos)

# # FILTER
# from dados import produtos
# def imprimir(iteravel):
#     print(*list(iteravel), sep='\n')
# # FILTRANDO E CRIANDO LISTAS NOVAS
# # novos_produtos = [
# #     produto
# #     for produto in produtos
# #     if produto['preco'] > 10
# # ]
# # FILTER
# novos_produtos = filter(
#     lambda x: x['preco'] > 10, # RETORNA VALOR QUANDO FUNÇÃO TRUE
#     produtos
# )
# imprimir(novos_produtos)

# REDUCE
# from functools import reduce
# from dados import produtos
# def soma(acumulador, produto):
#     return acumulador + produto['preco']
# total = reduce(
#     soma,
#     produtos,
#     0
# )
# print(total)
# total = 0
# for produto in produtos:
#     total += produto['preco']
# print(total)
# print(sum(produto['preco'] for produto in produtos))

# FUNÇÕES RECURSIVAS E RECURSIVIDADE
# numero = 5
# lista = []
# for i in range(numero, 0, -1):
#     lista.append(i)
# fatorial = 1
# for n in lista:
#     fatorial *= n
# print(fatorial)

# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     list = [i for i in range(n, 0, -1)]
#     factorial = 1
#     for n in list:
#         factorial *= n
#     return factorial
# print(factorial(9))

# def factorial(n):
#     if n <= 1:
#         return 1
#     return n*factorial(n-1)
# print(factorial(5))

# Criando arquivos com Python + Context Manager with
# Usamos a função open para abrir
# um arquivo em Python (ele pode ou não existir)
# Modos:
# r (leitura), w (escrita), x (para criação)
# a (escreve ao final), b (binário)
# t (modo texto), + (leitura e escrita)
# Context manager - with (abre e fecha)
# Métodos úteis
# write, read (escrever e ler)
# writelines (escrever várias linhas)
# seek (move o cursor)
# readline (ler linha)
# readlines (ler linhas)
# Módulo os:
# os.remove ou unlink - apaga o arquivo
# os.rename - troca o nome ou move o arquivo

# import os
# caminho_arquivo = '/home/bruna/Documentos/python/aula186.txt'
# arquivo = open(caminho_arquivo, 'w')
# arquivo.close()
# with open(caminho_arquivo, 'w') as arquivo:
#     arquivo.write('Linha 1\n')
#     arquivo.write('Linha 2\n')
#     arquivo.writelines(
#         ('Linha 3\n', 'Linha 4\n')
#     )
#     # arquivo.seek(0, 0)
# print(arquivo.read())
# print('Lendo')
# arquivo.seek(0, 0)
# print(arquivo.readline(), end='')
# print(arquivo.readline().strip())
# print(arquivo.readline().strip())

# print('READLINES')
# arquivo.seek(0, 0)
# for linha in arquivo.readlines():
#     print(linha.strip())
# with open(caminho_arquivo, 'r') as arquivo:
#     print(arquivo.read())

# os.remove(caminho_arquivo) # ou unlink
# os.rename(caminho_arquivo, 'aula116-2.txt')

# Módulo json:
# json.dump = Gera um arquivo json
# json.load
# import json

# pessoa = {
#     'nome': 'Luiz Otávio 2',
#     'sobrenome': 'Miranda',
#     'enderecos': [
#         {'rua': 'R1', 'numero': 32},
#         {'rua': 'R2', 'numero': 55},
#     ],
#     'altura': 1.8,
#     'numeros_preferidos': (2, 4, 6, 8, 10),
#     'dev': True,
#     'nada': None,
# }
# with open('aula117.json', 'w', encoding='utf8') as arquivo:
#     json.dump(
#         pessoa,
#         arquivo,
#         ensure_ascii=False,
#         indent=2,
#     )
# with open('aula117.json', 'r', encoding='utf8') as arquivo:
#     pessoa = json.load(arquivo)
#     # print(pessoa)
#     # print(type(pessoa))
#     print(pessoa['nome'])
