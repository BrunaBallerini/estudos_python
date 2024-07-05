# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# type: ignore

# GENERATOR FUNCTION
# generator = (n for n in range(10))

# def generator(n=0, maximum=10):
#     while True:
#         yield n # PAUSA
#         n += 1
#         if n >= maximum:
#             return

# gen = generator(maximum=50)
# for n in gen:
#     print(n)

# YIELD FROM
# def gen1():
#     print('COMECOU GEN1')
#     yield 1
#     yield 2
#     yield 3
#     print('ACABOU GEN1')

# def gen2():
#     print('COMECOU GEN2')
#     yield from gen1()
#     yield 10
#     yield 20
#     yield 30
#     print('ACABOU GEN2')

# generator = gen2()
# for i in generator:
#     print(i)

# def gen1():
#     print('COMECOU GEN1')
#     yield 1
#     yield 2
#     yield 3
#     print('ACABOU GEN1')

# def gen3():
#     print('COMECOU GEN3')
#     yield 10
#     yield 20
#     yield 30
#     print('ACABOU GEN3')

# def gen2(gen=None):
#     print('COMECOU GEN2')
#     if gen is not None:
#         yield from gen
#     yield 4
#     yield 5
#     yield 6
#     print('ACABOU GEN2')

# g1 = gen2(gen1())
# g2 = gen2(gen3())
# g3 = gen2()
# for numero in g1:
#     print(numero)
# print()
# for numero in g2:
#     print(numero)
# print()
# for numero in g3:
#     print(numero)
# print()

# TRY EXCEPT
# try:
#     a = 18
#     b = 0
#     c = a / b
# except ZeroDivisionError as e:
#     print(e.__class__.__name__)
#     print(e)
# except NameError:
#     print('Nome b não está definido')
# except (TypeError) as error:
#     print('MSG:', error)
#     print('Nome:', error.__class__.__name__)
# except Exception:
#     print('ERRO DESCONHECIDO.')
# else:
#     print('EXECUTA QUANDO NÃO DÁ ERRO.')
# finally:
#     print('SEMPRE SERÁ EXECUTADO.')

# RAISE - LANÇANDO EXCEÇÕES
# def nao_aceito_zero(d):
#     if d == 0:
#         raise ZeroDivisionError('Você está tentando dividir por zero')
#     return True
# def deve_ser_int_ou_float(n):
#     tipo_n = type(n)
#     if not isinstance(n, (float, int)):
#         raise TypeError(
#             f'"{n}" deve ser int ou float. '
#             f'"{tipo_n.__name__}" enviado.'
#         )
#     return True
# def divide(n, d):
#     deve_ser_int_ou_float(n)
#     deve_ser_int_ou_float(d)
#     nao_aceito_zero(d)
#     return n / d
# print(divide(8, '0'))

# import sys
# print(sys.platform)

# # import secao4_parte2
# from secao4_parte2 import variavel_modulo
# print('E este módulo se chama', __name__)
# # print(secao4_parte2.variavel_modulo)
# print(variavel_modulo)

# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)
# import copy
# from dados import produtos_modulo
# def p(lista):
#    for item in lista:
#     print(f'{item["nome"]} - R${item["preco"]:.2f}', sep='\n')

# def ordem_sort_nome(dicionario):
#   return dicionario['nome']

# def ordem_sort_preco(dicionario):
#   return dicionario['preco']

# novos_produtos = []
# for produto in produtos_modulo.produtos:
#     novos_produtos.append({**produto,
#           'preco': round(produto['preco'] * 1.10, 2)})
# print(*novos_produtos, sep='\n')
# print()
# # novos_produtos_lc = [
# #     {**produto, 'preco': produto['preco'] * 1.10}
# #     for produto in produtos
# # ]
# # print(novos_produtos_lc)
# # for produto in novos_produtos:
# #     print(f'{produto["nome"]} - R${produto["preco"]:.2f}', sep='\n')

# # Ordene os produtos por nome decrescente (do maior para menor)
# # Gere produtos_ordenados_por_nome por deep copy (cópia profunda)
# produtos_ordenados_por_nome = copy.deepcopy(novos_produtos)
# produtos_ordenados_por_nome.sort(reverse=True, key=ordem_sort_nome)
# p(produtos_ordenados_por_nome)
# print()

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)
# produtos_ord_preco = sorted(copy.deepcopy(novos_produtos),
#                   key=ordem_sort_preco)
# p(produtos_ord_preco)
# print()
# p(produtos_modulo.produtos)

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

# def soma(x, y):
#     return x + y
# def multiplica(x, y):
#     return x * y
# def criar_funcao(funcao, x):
#     def interna(y):
#         return funcao(x, y)
#     return interna
# soma_com_cinco = criar_funcao(soma, 5)
# tres_com_5 = soma_com_cinco(3)
# print(tres_com_5)
# multiplica_por_dez = criar_funcao(multiplica, 10)
# dois_por_dez = multiplica_por_dez(2)
# print(dois_por_dez)

# Variáveis livres + nonlocal (locals, globals)
# print(globals())
# def fora(x):
#     a = x
#     def dentro():
#         # print(locals())
#         return a
#     return dentro
# dentro1 = fora(10)
# dentro2 = fora(20)
# print(dentro1())
# print(dentro2())

# def concatenar(string_inicial):
#     valor_final = string_inicial
#     def interna(valor_a_concatenar=''):
#         nonlocal valor_final
#         valor_final += valor_a_concatenar
#         return valor_final
#     return interna
# c = concatenar('a')
# print(c('b'))
# print(c('c'))
# print(c('d'))
# print(c())

# FUNÇÕS DECORADAS E DECORADORAS
# Decorar = Adicionar / Remover/ Restringir / Alterar
# Decoradores são usados para fazer o Python usar as funções decoradoras em
# outras funções.

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
#        raise TypeError('Parametro deve ser uma string')

# inverte_string_checando_parametro = criar_funcao(inverte_string)
# invertida = inverte_string_checando_parametro('123', 'bruna')
# invertida = inverte_string('123', 'bruna')
# print(invertida)

# Exercício - Unir listas com a função zipper
# cidades = ['Salvador', 'Ubatuba', 'Belo Horizonte']
# estados = ['BA', 'SP', 'MG', 'RJ']
# cidades_estados = list(zip(cidades, estados))
# print(cidades_estados)

# # ZIP PARA DUAS LISTAS
# lista1 = [1, 2, 3, 4, 5, 6]
# lista2 = ['a', 'b', 'c']
# tamanho_minimo = min(len(lista1), len(lista2))
# resultado = []
# for i in range(tamanho_minimo):
#     tupla = (lista1[i], lista2[i])
#     resultado.append(tupla)
# print(resultado)

# # ZIP PARA VÁRIAS LISTAS
# def meu_zip(*args):
#     tamanho_minimo = min(len(lista) for lista in args)
#     resultado = []
#     for i in range(tamanho_minimo):
#         tupla = tuple(lista[i] for lista in args)
#         resultado.append(tupla)
#     return resultado
# def p(list):
#     for item in list:
#         print(item)
# lista1 = [1, 2, 3, 4, 5, 6]
# lista2 = ['a', 'b', 'c']
# lista3 = ['q', 'w', 'e', 'r']
# combinado = meu_zip(lista1, lista2, lista3)
# p(combinado)

# cidades = ['Salvador', 'Ubatuba', 'Belo Horizonte']
# estados = ['BA', 'SP', 'MG', 'RJ']
# cidades_estados = meu_zip(cidades, estados)
# p(cidades_estados)

# from itertools import zip_longest
# cidades = ['Salvador', 'Ubatuba', 'Belo Horizonte']
# estados = ['BA', 'SP', 'MG', 'RJ']
# cidades_estados = list(zip_longest(cidades, estados))
# print(cidades_estados)

# Considerando duas listas de inteiros ou floats (lista A e lista B)
# Some os valores nas listas retornando uma nova lista com os valores somados:
# Se uma lista for maior que a outra, a soma só vai considerar o tamanho da
# menor.

# lista_a = [1, 2, 3, 4, 5, 6, 7]
# lista_b = [1, 2, 3, 4]

# def soma_de_listas(*args):
#     tamanho_minimo = min(len(lista) for lista in args)
#     resultado = []
#     for i in range(tamanho_minimo):
#             soma = sum(lista[i] for lista in args if len(lista) > i)
# GARANTE QUE A SOMA SEJA FEITA SOMENTE SE A LISTA TIVER ELEMENTOS NO INDICE
#             resultado.append(soma)
#     return resultado

# somatorio = soma_de_listas(lista_a, lista_b)
# print(somatorio)

# lista_a = [10, 2, 3, 40, 5, 6, 7]
# lista_b = [1, 2, 3, 4]
# lista_soma = []
# for x, y in zip(lista_a, lista_b):
#     soma = x + y
#     lista_soma.append(soma)
# # lista_soma = [x + y for x, y in zip(lista_a, lista_b)]
# print(lista_soma)

# lista_soma = []
# for i in range(len(lista_b)):
#     lista_soma.append(lista_a[i] + lista_b[i])
# print(lista_soma)

# lista_soma = []
# for i, _ in enumerate(lista_b):
#     lista_soma.append(lista_a[i] + lista_b[i])
# print(lista_soma)
