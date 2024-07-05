# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# type: ignore

# import os

# lista_compras = []
# quant_itens = ''
# acao = ''
# while True:
#     acao = input('Digite o que você gostaria de fazer na lista de compras \n'
#                      '[A]DICIONAR [AP]AGAR [L]ISTAR [S]AIR:').lower()

#     if acao == 'a':
#         quant_itens = input('Digite a quantidade de itens da lista: ')

#         if quant_itens.isdigit():
#             quant_itens_int = int(quant_itens)
#         else:
#             os.system('clear')
#             print('Digite valores para inserir na lista.')
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
#                 print('Vão será possível retirar pois não existe.')
#             else:
#                 lista_compras.remove(retirada)
#                 os.system('clear')
#                 print(lista_compras)
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


# palavra_usuario = []
# for letra in palavra_base:
#     palavra_usuario += '*'

# while True:
#     chute_letra = input('Digite uma letra: ').lower().strip()
#     if len(chute_letra) > 1:
#         print('Digite apenas uma letra: ')
#         continue

#     index = 0
#     for letra in palavra_base:
#         if letra == chute_letra:
#             palavra_usuario[index] = letra
#         index += 1
#     print(palavra_usuario)

#     tentativas += 1

#     if palavra_base == palavra_usuario:
#         print('Você acertou!')
#         print(f'Tentativas: {tentativas}')
#         break

# tentativas = 0
# palavra_secreta = 'banana'
# letras_acertadas = ''

# while True:

#     chute_letra = input('Digite uma letra: ').lower().strip()

#     if len(chute_letra) > 1:
#         print('Digite apenas uma letra: ')
#         continue

#     if chute_letra in palavra_secreta:
#         letras_acertadas += chute_letra
#     palavra_usuario = ''
#     for letra in palavra_secreta:
#         if letra in letras_acertadas:
#             palavra_usuario += letra
#         else:
#             palavra_usuario += '*'
#     print(palavra_usuario)

#     tentativas += 1

#     if palavra_secreta == palavra_usuario:
#         os.system('clear')
#         print(f'Você acertou! A palavra era: {palavra_secreta}')
#         print(f'Tentativas: {tentativas}')
#         break


# CLOSURE - ADIANDO EXECUÇÃO DE FUNÇÕES
# def criar_multiplicador(multiplicador):
#     def multiplicar (numero):
#         return numero * multiplicador
#     return multiplicar

# quadruplo = criar_multiplicador(4)
# print(quadruplo(2))

# quintuplo = criar_multiplicador(5)
# print(quintuplo(10))

# def criar_somatório(x):
#     def soma(y):
#         return x + y
#     return soma

# def criar_multiplicacao(x):
#     def multiplicacao(y):
#             return x * y
#     return multiplicacao

# def criar_funcao(funcao, *args):
#     return funcao(*args)

# soma_com_cinco = criar_funcao(criar_somatório, 5)
# tres_com_cinco = soma_com_cinco(3)
# print(tres_com_cinco)

# multiplica_por_dez = criar_funcao(criar_multiplicacao, 10)
# dois_por_dez = multiplica_por_dez(2)
# print(dois_por_dez)

# def criar_funcao(func):
#     def interna(*args):
#         for arg in args:
#             e_string(arg)
#         # resultados = []
#         # for arg in args:
#         #     resultado = func(arg)
#         #     resultados.append(resultado)
#         resultados = [
#             func(arg)
#             for arg in args
#         ]
#         return f'O seu resultado foi {resultados}.'
#     return interna

# @criar_funcao # DECORADOR
# def inverte_string(string):
#     return string[::-1] # [INICIO:FIM:PASSO]

# def e_string(param):
#     if not isinstance(param, str):
#         raise TypeError('Parametro deve ser uma string')

# # inverte_string_checando_parametro = criar_funcao(inverte_string)
# # invertida = inverte_string_checando_parametro('123', 'bruna')
# invertida = inverte_string('123', 'bruna')
# print(invertida)


# def slot_1(status_bar_):
#     def inner():
#         status_bar_.showMessage('Slot Executado')
#     return inner

# def slot_3(action):
#     def inner():
#         slot_2(action.isChecked())
#     return inner

# status_bar = window.statusBar()
# status_bar.showMessage('Mostrar mensagem na barra')

# menu_bar = window.menuBar()
# primeiro_menu = menu_bar.addMenu('Menu 1')
# primeira_acao = primeiro_menu.addAction('Ação 1')

# primeira_acao.triggered.connect(slot_1(status_bar))
# OU
# primeira_acao.triggered.connect(lambda: slot_1(status_bar))
