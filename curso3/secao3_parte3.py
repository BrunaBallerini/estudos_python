# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# type: ignore

# import os
# palavra = list("BANANA")
# letra = 'A'
# nova_palavra = []
# for caractere in palavra:
#     if caractere == letra:
#         nova_palavra.append(caractere)
# print(nova_palavra)

# cores = ['azul', 'amarelo', 'vermelho', 'preto', 'verde']
# cores.append('roxo')
# for cor in cores:
#     print(cores.index(cor), cor)
# print()
# for index, cor in enumerate(cores):
#     print(index, cor)
# print()
# index = 0
# for cor in cores:
#     print(index, cor)
#     index += 1
# print()
# indices = range(len(cores))
# for indice in indices:
#     print(indice, cores[indice])

# """
# Introdução ao empacotamento e desempacotamento
# """
# _, _, nome, *resto = ['Maria', 'Helena', 'Luiz']
# print(nome)

# """
# enumerate - enumera iteráveis (índices)
# """
# # [(0, 'Maria'), (1, 'Helena'), (2, 'Luiz'), (3, 'João')]
# lista = ['Maria', 'Helena', 'Luiz']
# lista.append('João')

# for indice, nome in enumerate(lista):
#     print(indice, nome, lista[indice])
# for item in enumerate(lista):
#     indice, nome = item
#     print(indice, nome)
# for tupla_enumerada in enumerate(lista):
#     print('FOR da tupla:')
#     for valor in tupla_enumerada:
#         print(f'\t{valor}')

# lista_compras = []
# quant_itens = ''
# acao = ''
# while True:
#     acao = input('Digite o que você gostaria de fazer na lista de compras \n'
#                      '[1]ADICIONAR [2]APAGAR [3]LISTAR [4]SAIR:')

#     if acao.isdigit():
#         acao_int = int(acao)
#     else:
#         os.system('clear')
#         print('Digite um valor válido.')
#         continue

#     if acao_int == 1:
#         quant_itens = input('Digite a quantidade de itens da lista: ')

#         if quant_itens.isdigit():
#             quant_itens_int = int(quant_itens)
#         else:
#             print('Digite valores para inserir na lista.')
#             continue

#         for item in range(quant_itens_int):
#             item = input('Digite o item:')
#             lista_compras.append(item)
#         os.system('clear')
#         print(lista_compras)

#     if len(lista_compras) > 0:
#         if acao_int == 2:
#             print(f'Sua lista tem {len(lista_compras)} itens.')
#             retirada = input('Digite o que você quer retirar: ')
#             if retirada not in lista_compras:
#                 os.system('clear')
#                 print('Vão será possível retirar pois não existe.')
#             else:
#                 lista_compras.remove(retirada)
#                 os.system('clear')
#                 print(lista_compras)

#         if acao_int == 3:
#             os.system('clear')
#             for indice, item in enumerate(lista_compras):
#                 print(f'{indice} - {item}')
#     else:
#         os.system('clear')
#         print('Não será permitido retirar item ou listar - Lista Vazia.')

#     if acao_int == 4:
#         break

# lista_compras = []
# quant_itens = ''
# acao = ''
# while True:
#     acao = input('Digite o que você gostaria de fazer na lista de compras \n'
#                      '[A]DICIONAR [AP]AGAR [L]ISTAR [S]AIR:').lower()

#     if acao == 'a':
#         quant_itens = input('Digite a quant. para inserir na lista: ')

#         if quant_itens.isdigit():
#             quant_itens_int = int(quant_itens)
#         else:
#             os.system('clear')
#             print('Você não digitou um número!')
#             continue
#         for item in range(quant_itens_int):
#             item = input('Digite o item:')
#             lista_compras.append(item)
#         os.system('clear')
#         print(lista_compras)

#     elif acao == 'ap':
#         if len(lista_compras) > 0:
#             print(f'Sua lista tem {len(lista_compras)} itens.')
#             retirada = input('Digite o que você quer retirar: ')
#             if retirada not in lista_compras:
#                 os.system('clear')
#                 print('Não será possível retirar este item pois não existe.')
#             else:
#                 lista_compras.remove(retirada)
#                 os.system('clear')
#                 print(lista_compras)
#                 #indice = int(indice_str)
#                 #del lista[indice]
#         else:
#             os.system('clear')
#             print('Não será permitido retirar item.')

#     elif acao == 'l':
#         if len(lista_compras) > 0:
#             os.system('clear')
#             for indice, item in enumerate(lista_compras):
#                 print(f'{indice} - {item}')
#         else:
#             os.system('clear')
#             print('Lista Vazia.')

#     elif acao == 's':
#         break

# """
# split e join com list e str
# split - divide uma string (list)
# join - une uma string
# """
# frase = '   Olha só que   , coisa interessante
# -> Transforma string em lista usando a separação dos itens passado como argmt
# lista_frases_cruas = frase.split(',') #.slit()
# lista_frases = []
# for indice, frases in enumerate(lista_frases_cruas):
# -> Retira espaços do começo e do fim da string
#     lista_frases.append(lista_frases_cruas[indice].strip()) #.strip()
# print(lista_frases_cruas)
# print(lista_frases)
# frases_unidas = ', '.join(lista_frases)
# print(frases_unidas)

# # Desempacotamento em chamadas de métodos e funções
# string = 'ABCD'
# lista = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']
# tupla = 'Python', 'é', 'legal'
# salas = [
#     # 0        1
#     ['Maria', 'Helena', ],  # 0
#     # 0
#     ['Elaine', ],  # 1
#     # 0       1       2
#     ['Luiz', 'João', 'Eduarda', ],  # 2
# ]
# p, b, *_, ap, u = lista
# print(p, u, ap)
# print('Maria', 'Helena', 1, 2, 3, 'Eduarda')
# print(*lista)
# print(*string)
# print(*tupla)
# print(*salas, sep='\n')

# """
# Operação ternária (condicional de uma linha)
# <valor> if <condicao> else <outro valor>
# """
# # condicao = 10 == 11
# # variavel = 'Valor' if condicao else 'Outro valor'
# # print(variavel)
# # digito = 9  # > 9 = 0
# # novo_digito = digito if digito <= 9 else 0
# # novo_digito = 0 if digito > 9 else digito
# # print(novo_digito)
# print('Valor' if False else 'Outro valor' if False else 'Fim')

# cpf = input("Digite os primeiros 9 dígitos do CPF:")

# # TRANSFORMANDO STRING EM LISTA E DEPOIS EM LISTA DE INTEIROS
# # cpf_lista = list(cpf)
# cpf_sem_ponto = cpf.split('.') # RETIREI O PONTO
# # print(cpf_sem_ponto)
# # CRIA A LISTA
# cpf_lista = []
# for digito in cpf_sem_ponto:
#     for n in digito:
#         cpf_lista.append(n)

# cpf_lista_int = []
# for digito in cpf_lista:
#     try:
#         digito_int = int(digito)
#         cpf_lista_int.append(digito_int)
#     except ValueError:
#         print('Você digitou uma letra!')
# # print(cpf_lista_int)

# # # CRIANDO UMA LISTA PARA MULTIPLICAÇÃO - VALIDAÇÃO PARTE 1
# lista_validacao_multiplicacao = []
# for x in range(10, 1, -1):
#     lista_validacao_multiplicacao.append(x)
# # print(lista_validacao_multiplicacao)

# # # MULTIPLICANDO E SOMATÓRIO DOS VALORES MULTIPLICADOS - VALIDAÇÃO PARTE 1
# lista_validacao_parte_1 = []
# somatorio_multiplicacao = 0
# for digito, x in zip(cpf_lista_int, lista_validacao_multiplicacao):
#     y = digito * x
#     lista_validacao_parte_1.append(y)
#     somatorio_multiplicacao += y
# # print(lista_validacao_parte_1, somatorio_multiplicacao)

# # SOMATÓRIO SEPARADO
# # somatorio = 0
# # for n in lista_validacao_parte_1:
# #     somatorio += n
# # print(somatorio)

# EXPLICAÇÃO ZIP:
# x = [1, 2, 3]
# y = [4, 5, 6]
# zipped = zip(x, y)
# print(list(zipped))
# x2, y2 = zip(*zip(x, y))
# x == list(x2) and y == list(y2)
# print(x2)
# print(y2)
# # ADENDO (NÃO É O CASO - SOMENTE INDICES)
# # x = [10, 20, 30]
# # indexes = range(len(x))
# # for index in indexes:
# #     print(index, x[index])
# # for index, i in enumerate(x):
# #     print(index, i)

# # MULTIPLICA SOMATÓRIO POR 10 E RESTO DA DIVISÃO POR 11
# multiplicacao_10 = somatorio_multiplicacao * 10
# # print(multiplicacao_10)
# resto_divisao_11 = multiplicacao_10 % 11
# # print(resto_divisao_11)

# # IF TERNÁRIO
# penultimo_digito = resto_divisao_11 if resto_divisao_11 <= 9 else 0
# print(resto_divisao_11, penultimo_digito)

# # IF NORMAL
# # if resto_divisao_11 <= 9:
# #     penultimo_digito = resto_divisao_11
# # else:
# #     penultimo_digito = 0
