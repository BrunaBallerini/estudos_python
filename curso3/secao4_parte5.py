# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# type: ignore

# Exercício - Lista de tarefas com desfazer e refazer
# import os
# import json

# def imprimir_lista(lista_de_tarefas):
#     if not lista_de_tarefas:
#         print('\nNada a ser listado. \n')
#         return
#     print()
#     print('TAREFAS:')
#     for item in lista_de_tarefas:
#         print(item)
#     print()


# def desfazer(lista_de_tarefas, lista_de_tarefas_desfeitas):
#     if not lista_de_tarefas:
#         print('\nNada a desfazer\n')
#         return
#     desfeito = lista_de_tarefas.pop()
#     lista_de_tarefas_desfeitas.append(desfeito)


# def refazer(lista_de_tarefas, lista_de_tarefas_desfeitas):
#     if not lista_de_tarefas_desfeitas:
#         print('\nNada a refazer\n')
#         return
#     refazer = lista_de_tarefas_desfeitas[-1]
#     lista_de_tarefas.append(refazer)
#     lista_de_tarefas_desfeitas.pop()


# def adicionar(entrada_usuário, lista_de_tarefas):
#     print()
#     entrada_usuario.strip().lower()
#     if not entrada_usuario:
#         print('Você não digitou uma tarefa.')
#         return
#     lista_de_tarefas.append(entrada_usuario)
#     imprimir_lista(lista_de_tarefas)

# def salvar(lista_de_tarefas, caminho):
#     dados = lista_de_tarefas
#     with open(caminho, 'w', encoding='utf8') as arquivo:
#         dados = json.dump(
# lista_de_tarefas,
# arquivo,
# indent=2,
# ensure_ascii=False
# )
#     return dados

# def ler(lista_de_tarefas, caminho):
#     dados = []
#     try:
#         with open(caminho, 'r', encoding='utf8') as arquivo:
#             dados = json.load(arquivo)
#     except FileNotFoundError:
#         salvar(lista_de_tarefas, caminho)
#     return dados


# CAMINHO_ARQUIVO = 'lista_tarefas.json'
# INICIALIZAÇÃO DA LISTA, ZERADA OU COM CONTEÚDO
# lista_de_tarefas = ler([], CAMINHO_ARQUIVO)
# lista_de_tarefas_desfeitas = []
# while True:
#     print('Comandos: listar, desfazer, refazer, sair')
#     entrada_usuario = input('Digite uma tarefa ou comando:')

#     if entrada_usuario == 'listar':
#         imprimir_lista(lista_de_tarefas)
#         ler(lista_de_tarefas, CAMINHO_ARQUIVO)
#     elif entrada_usuario == 'desfazer':
#         desfazer(lista_de_tarefas, lista_de_tarefas_desfeitas)
#         imprimir_lista(lista_de_tarefas)
#         salvar(lista_de_tarefas, CAMINHO_ARQUIVO)
#     elif entrada_usuario == 'refazer':
#         refazer(lista_de_tarefas, lista_de_tarefas_desfeitas)
#         imprimir_lista(lista_de_tarefas)
#         salvar(lista_de_tarefas, CAMINHO_ARQUIVO)
#     elif entrada_usuario == 'clear':
#         os.system('clear')
#     elif entrada_usuario == 'sair':
#         break
#     else:
#         adicionar(entrada_usuario, lista_de_tarefas)
#         salvar(lista_de_tarefas, CAMINHO_ARQUIVO)

# SÓ FINALIZA QUANDO TERMINA O WHILE
# with open('lista_tarefas.json', 'w') as arquivo:
#     json.dump(
#         lista_de_tarefas,
#         arquivo,
#         ensure_ascii=False,
#         indent=2,
#     )

# while True:
#     print('Comandos: listar, desfazer e refazer')
#     entrada_usuario = input('Digite uma tarefa ou comando: ')

#     comandos = {
#         'listar': lambda: imprimir_lista(lista_de_tarefas),
#         'desfazer': lambda: desfazer(lista_de_tarefas, \
#               lista_de_tarefas_desfeitas),
#         'refazer': lambda: refazer(lista_de_tarefas, \
#               lista_de_tarefas_desfeitas),
#         'clear': lambda: os.system('clear'),
#         'adicionar': lambda: adicionar(entrada_usuario, lista_de_tarefas),
#     }
#     comando = comandos.get(entrada_usuario)
#           if comandos.get(entrada_usuario) is not None else \
#         comandos['adicionar']
#     comando()
