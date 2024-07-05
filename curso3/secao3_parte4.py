# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# type: ignore

# import sys
# import random
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

# # EXPLICAÇÃO ZIP:
# # x = [1, 2, 3]
# # y = [4, 5, 6]
# # zipped = zip(x, y)
# # print(list(zipped))
# # x2, y2 = zip(*zip(x, y))
# # x == list(x2) and y == list(y2)
# # print(x2)
# # print(y2)
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

# # MEU DESENVOLVIMENTO:
# cpf = input("Digite os primeiros 9 dígitos do CPF:")
# # TRANSFORMANDO STRING EM LISTA E DEPOIS EM LISTA DE INTEIROS
# cpf_sem_ponto = ''.join(filter(str.isdigit, cpf))
# nove_digitos_cpf = cpf_sem_ponto[:9]
# # CRIA A LISTA DE INTEIROS
# cpf_lista = list(nove_digitos_cpf)
# # CRIAÇÃO PRIMEIRO DÍGITO
# somatorio_digito_1 = 0
# contador_reverso_1 = 10
# for digito in cpf_lista:
#     somatorio_digito_1 += int(digito) * contador_reverso_1
#     contador_reverso_1 -= 1
# resto_divisao_11 = (somatorio_digito_1 * 10) % 11
# penultimo_digito = resto_divisao_11 if resto_divisao_11 <= 9 else 0
# # CRIAÇÃO SEGUNDO DÍGITO
# cpf_lista.append(penultimo_digito)
# somatorio_digito_2 = 0
# contador_reverso_2 = 11
# for digito in cpf_lista:
#     somatorio_digito_2 += int(digito) * contador_reverso_2
#     contador_reverso_2 -= 1
# resto_divisao_2 = (somatorio_digito_2 * 10) % 11
# ultimo_digito = resto_divisao_2 if resto_divisao_2 <= 9 else 0
# cpf_lista.append(ultimo_digito)
# # VOLTANDO À STRING`
# cpf_final = ''
# for digito in cpf_lista:
#     cpf_final += f'{digito}'
# print(cpf_final)

# # DESENVOLVIMENTO PROFESSOR:
# cpf_usuario = input("Digite seu CPF sem pontos:")
# # REMOVENDO CARACTERES QUE NÃO SEJAM DIGITOS
# #-> OPÇÃO
# cpf_sem_ponto = cpf_usuario.replace('.', '').replace('-', '').replace(' ','')
# cpf_sem_ponto = ''.join(filter(str.isdigit, cpf_usuario))
# # CERTIFICANDO PEGAR SOMENTE OS 9 PRIMEIROS DIGITOS
# nove_digitos_cpf = cpf_sem_ponto[:9]
# # CRIAÇÃO PRIMEIRO DÍGITO
# contador_reverso_1 = 10
# somatorio_digito_1 = 0
# for digito in nove_digitos_cpf:
#     somatorio_digito_1 += (int(digito) * contador_reverso_1)
#     contador_reverso_1 -= 1
# resto_divisao_11 = (somatorio_digito_1 * 10) % 11
# penultimo_digito = resto_divisao_11 if resto_divisao_11 <= 9 else 0
# # CRIAÇÃO SEGUNDO DÍGITO
# dez_digitos_cpf = f'{nove_digitos_cpf}{penultimo_digito}'
# contador_reverso_2 = 11
# somatorio_digito_2 = 0
# for digito in dez_digitos_cpf:
#     somatorio_digito_2 += (int(digito) * contador_reverso_2)
#     contador_reverso_2 -= 1
# resto_divisao_11 = (somatorio_digito_2 * 10) % 11
# ultimo_digito = resto_divisao_11 if resto_divisao_11 <= 9 else 0
# cpf_calculado = f'{dez_digitos_cpf}{ultimo_digito}'

# if cpf_sem_ponto == cpf_calculado:
#     print(f'{cpf_calculado} é valido.')
# else:
#     print('CPF inválido.')

# # DESENVOLVIMENTO PROFESSOR:
# cpf_usuario = input("Digite seu CPF sem pontos:")
# cpf_sem_ponto = ''.join(filter(str.isdigit, cpf_usuario))

# verificacao_digitos_iguais = cpf_usuario == cpf_usuario[0] * len(cpf_usuario)
# if verificacao_digitos_iguais:
#     print('Você digitou somente digitos iguais. ')
#     sys.exit()

# nove_digitos_cpf = cpf_sem_ponto[:9]
# contador_reverso_1 = 10
# somatorio_digito_1 = 0
# for digito in nove_digitos_cpf:
#     somatorio_digito_1 += (int(digito) * contador_reverso_1)
#     contador_reverso_1 -= 1
# resto_divisao_11 = (somatorio_digito_1 * 10) % 11
# penultimo_digito = resto_divisao_11 if resto_divisao_11 <= 9 else 0

# dez_digitos_cpf = f'{nove_digitos_cpf}{penultimo_digito}'
# contador_reverso_2 = 11
# somatorio_digito_2 = 0
# for digito in dez_digitos_cpf:
#     somatorio_digito_2 += (int(digito) * contador_reverso_2)
#     contador_reverso_2 -= 1
# resto_divisao_11 = (somatorio_digito_2 * 10) % 11
# ultimo_digito = resto_divisao_11 if resto_divisao_11 <= 9 else 0
# cpf_calculado = f'{dez_digitos_cpf}{ultimo_digito}'

# if cpf_sem_ponto == cpf_calculado:
#     print(f'{cpf_calculado} é valido.')
# else:
#     print('CPF inválido.')

# # GERADOR CPF:
# nove_digitos_cpf = ''
# for i in range(9):
#     randomico = random.randint(0, 9
#     nove_digitos_cpf += f'{randomico}'

# contador_reverso_1 = 10
# somatorio_digito_1 = 0
# for digito in nove_digitos_cpf:
#     somatorio_digito_1 += (int(digito) * contador_reverso_1)
#     contador_reverso_1 -= 1
# resto_divisao_11 = (somatorio_digito_1 * 10) % 11
# penultimo_digito = resto_divisao_11 if resto_divisao_11 <= 9 else 0

# dez_digitos_cpf = f'{nove_digitos_cpf}{penultimo_digito}'
# contador_reverso_2 = 11
# somatorio_digito_2 = 0
# for digito in dez_digitos_cpf:
#     somatorio_digito_2 += (int(digito) * contador_reverso_2)
#     contador_reverso_2 -= 1
# resto_divisao_11 = (somatorio_digito_2 * 10) % 11
# ultimo_digito = resto_divisao_11 if resto_divisao_11 <= 9 else 0

# cpf_calculado = f'{dez_digitos_cpf}{ultimo_digito}'
# print(cpf_calculado)
