# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# type: ignore

# def fatorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * fatorial(n-1)


# print(fatorial(4))

# primeiro_valor = input('Digite um valor: ')
# segundo_valor = input('Digite outro valor: ')
# if primeiro_valor >= segundo_valor:
#     print(f'{primeiro_valor=} é maior ou igual do que o {segundo_valor=}')
# else:
#     print(f'{segundo_valor=} é maior do que o {primeiro_valor=}')

# entrada = input('[E]ntrar [S]air: ')
# senha_digitada = input('Senha: ')
# senha_permitida = '123456'
# if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
#     print('Entrar')
# else:
#     print('Sair')

# senha = input('Digite a senha: ')
# if not senha:
#     print('Você não digitou a senha.')

# Avaliação de curto circuito
# print(True and True and False)
# print(True or False or '')
# senha = input('Senha: ') or 'Sem senha'
# print(senha)

# nome = input('Digite seu nome: ')
# encontrar = input('Digite o que deseja encontrar: ')
# if encontrar in nome:
#     print(f'{encontrar} está em {nome}')
# else:
#     print(f'{encontrar} não está em {nome}')

# """
# s - string
# d e i - int
# f - float
# x e X - Hexadecimal (ABCDEF0123456789)
# """
# nome = 'Luiz'
# preco = 1000.95897643
# variavel = '%s, o preço é R$%.2f' % (nome, preco)
# print(variavel)
# print('O hexadecimal de %d é %08X' % (1500, 1500))

# """
# s - string
# d - int
# f - float
# .<número de dígitos>f
# x ou X - Hexadecimal
# (Caractere)(><^)(quantidade)
# > - Esquerda
# < - Direita
# ^ - Centro
# = - Força o número a aparecer antes dos zeros
# Sinal - + ou -
# Ex.: 0>-100,.1f
# Conversion flags - !r !s !a
# """
# variavel = 'ABC'
# print(f'{variavel}')
# print(f'{variavel: >10}')
# print(f'{variavel: <10}.')
# print(f'{variavel: ^10}.')
# print(f'{1000.4873648123746:0=+10,.1f}')
# print(f'O hexadecimal de 1500 é {1500:08X}')
# print(f'{variavel!r}')

# """
# Fatiamento de strings
#  012345678
#  Olá mundo
# -987654321
# Fatiamento [inicio:final:passo] [::]
# Obs.: a função len retorna a qtd
# de caracteres da str
# """
# variavel = 'Olá mundo'
# print(variavel[-1:-10:-1]) # INVERTE STRING

# nome = input('Digite seu nome: ')
# idade = input('Digite sua idade: ')
# if nome and idade:
#     print(f'Seu nome é {nome}\nSeu nome invertido é {nome[::-1]}')
#     print(f'Seu nome contem espaços: {" " in nome}')
#     print(f'Seu nome tem {len(nome)} letras')
#     print(f'A primeira letra do seu nome é {nome[0]}')
#     print(f'A última letra do seu nome é {nome[-1]}')
# elif not nome or not idade:
#     print('Desculpe, você deixou campos vazios.')

# print(True and True and False) # FALSE
# print(True or False or '') # TRUE

# """
# Flag (Bandeira) - Marcar um local
# None = Não valor
# is e is not = é ou não é (tipo, valor, identidade)
# id = Identidade
# """
# condicao = False
# passou_no_if = None
# if condicao:
#     passou_no_if = True
#     print('Faça algo')
# else:
#     print('Não faça algo')
# if passou_no_if is None:
#     print('Não passou no if')
# else:
#     print('Passou no if')

# numero = input('Digite um número: ')
# try:
#     numero_int = int(numero)
#     if numero_int % 2 == 0:
#         print(f'{numero_int} é par.')
#     else:
#         print(f'{numero_int} é ímpar.')
# except:
#     print('Digite um número inteiro.')

# numero = input('Digite um número: ')
# if numero.isdigit():
#     numero_int = int(numero)
#     if numero_int % 2 == 0:
#         print(f'{numero_int} é par.')
#     else:
#         print(f'{numero_int} é ímpar.')
# else:
#     print('Digite um número inteiro.')

# numero = input('Digite um número: ')
# if numero.isdigit():
#     numero_int = int(numero)
#     par_impar = numero_int % 2 == 0
#     if par_impar:
#         par_impar_texto =  'par'
#     else:
#         par_impar_texto = 'ímpar'
#     print(f'{numero_int} é {par_impar_texto}')
# else:
#     print('Digite um número inteiro.')

# hora_str = input('Digite a hora em número inteiro: ')
# try:
#     hora_int = int(hora_str)
#     if 0 <= hora_int <= 11:
#         saudacao = 'Bom dia.'
#     elif 12 <= hora_int <= 17:
#         saudacao = 'Boa tarde.'
#     elif 18 <= hora_int <= 23:
#         saudacao = 'Boa noite.'
#     else:
#         saudacao = 'Você não digitou corretamente.'
#     print(saudacao)
# except ValueError:
#     print('Você não digitou um número inteiro.')

# nome = input('Digite o seu nome: ')
# nome_sendo_numero = nome.isdigit()
# nome_nao_sendo_numero = not nome.isdigit()
# tamanho_nome = len(nome)
# if nome and nome_nao_sendo_numero:
#     if tamanho_nome <= 4:
#         print('Seu nome é curto.')
#     elif 5 <= tamanho_nome <= 6:
#         print('Seu nome tem o tamanho normal.')
#     else:
#         print('Seu nome é muito grande.')
# elif nome_sendo_numero:
#     print('Você digitou um número.')
# elif not nome:
#     print('Você não digitou nenhum nome.')

# par_impar = 51
# par_impar %= 2
# print(par_impar)
# contador = 5
# contador *= '2'
# print(contador)

# qtd_linhas = 5
# qtd_colunas = 5
# linha = 1
# while linha <= qtd_linhas:
#     coluna = 1
#     while coluna <= qtd_colunas:
#         print(f'{linha=} {coluna=}')
#         coluna+=1
#     linha+=1
# print('Acabou')

# for linha in range(1,6):
#     for coluna in range(1,6):
#         print(f'{linha=} {coluna=}')

# for i in range(5):
#     for j in range(i + 1):
#         print(j + 1, end = ' ')
#     print()

# nome = 'BRUNA BALLERINI'
# tamanho_nome = len(nome)
# posicao = 0
# while posicao < tamanho_nome:
#     novo_nome = f' {nome[posicao]} '
#     print(novo_nome, end = '')
#     # print(nome[posicao])
#     posicao += 1

# nome = 'BRUNA BALLERINI'
# tamanho_nome = len(nome)
# posicao = 0
# novo_nome = ''
# while posicao < tamanho_nome:
#     novo_nome += nome[posicao]
#     posicao += 1
# print(novo_nome)

# nome = 'BRUNA BALLERINI'
# for letra in nome:
#     print(letra)

# nome = list('BRUNA FERNANDES')
# outro_nome = []
# for letra in nome:
#     outro_nome.append(letra)
# print(outro_nome)

# numero1 = input('Digite o primeiro número: ')
# numero2 = input('Digite o segundo número: ')
# operador = input('Digite qual operação quer que seja realizada: ')
# parada = ''
# try:
#     numero1_int = float(numero1)
#     numero2_int = float(numero2)
#     while parada != 'S' or parada == 's':
#         if operador == '+':
#             resultado = numero1_int + numero2_int
#             print(f'SOMA = {resultado}')
#         elif operador == '-':
#             resultado = numero1_int - numero2_int
#             print(f'SUBTRAÇÃO = {resultado}')
#         elif operador == '/':
#             resultado = numero1_int / numero2_int
#             print(f'DIVISÃO = {resultado}')
#         elif operador == '*':
#             resultado = numero1_int * numero2_int
#             print(f'MULTIPLICAÇÃO = {resultado}')
#         else:
#             print('Digite um operador válido!')
#         parada = input('Digite "S" para sair ou outra tecla para continuar.')

#         if parada == 'S' or parada == 's':
#             break

#         operador = input('Digite qual outra oper. quer que seja realizada: ')
# except:
#     print('Vocẽ não digitou um número válido. ')

# parada = ''
# while parada == '':
#     try:
#         numero1 = input('Digite o primeiro número: ')
#         operador = input('Digite qual operação quer que seja realizada: ')
#         numero2 = input('Digite o segundo número: ')

#         numero1_int = float(numero1)
#         numero2_int = float(numero2)
#         soma = operador == '+'
#         subtraçao = operador == '-'
#         divisao = operador == '/'
#         multiplicacao = operador == '*'

#         if soma:
#             resultado = numero1_int + numero2_int
#             print(f'SOMA = {resultado}')
#         elif subtraçao:
#             resultado = numero1_int - numero2_int
#             print(f'SUBTRAÇÃO = {resultado}')
#         elif multiplicacao:
#             resultado = numero1_int * numero2_int
#             print(f'MULTIPLICAÇÃO = {resultado}')
#         elif divisao:
#             if numero2_int == 0:
#                 print('ERRO! Divisão por 0.')
#             else:
#                 resultado = numero1_int / numero2_int
#                 print(f'DIVISÃO = {resultado}')
#         else:
#             print('Operador inválido!')

#         parada = input('Digite "S" para sair ou outra tecla para continuar.')
#         if parada == 'S' or parada == 's':
#             break

#     except:
#         print('Vocẽ não digitou um número válido. ')


# while True:
#     try:
#         numero1 = input('Digite o primeiro número: ')
#         numero2 = input('Digite o segundo número: ')
#         operador = input('Digite qual operação (+-/*): ')
#         numero1_float = float(numero1)
#         numero2_float = float(numero2)

#         soma = operador == '+'
#         subtraçao = operador == '-'
#         divisao = operador == '/'
#         multiplicacao = operador == '*'

#         if soma:
#             resultado = numero1_float + numero2_float
#             print(f'SOMA = {resultado}')
#         elif subtraçao:
#             resultado = numero1_float - numero2_float
#             print(f'SUBTRAÇÃO = {resultado}')
#         elif multiplicacao:
#             resultado = numero1_float * numero2_float
#             print(f'MULTIPLICAÇÃO = {resultado}')
#         elif divisao:
#             if numero2_float == 0:
#                 print('ERRO! Divisão por 0.')
#             else:
#                 resultado = numero1_float / numero2_float
#                 print(f'DIVISÃO = {resultado}')
#         else:
#             print('Operador inválido!')

#         sair = input('digite "s" para sair ou outra tecla para continuar.') \
#                                   .lower().startswith('s')
#         if sair:
#             break
#     except:
#         print('Vocẽ não digitou um número válido. ')


# while True:
#     numero1 = input('Digite o primeiro número: ')
#     numero2 = input('Digite o segundo número: ')
#     operador = input('Digite qual operação quer que seja realizada (+-/*): ')

#     numeros_validos = True #FLAG
#     numero1_float = 0
#     numero2_float = 0
#     try:
#         numero1_float = float(numero1)
#         numero2_float = float(numero2)
#     except:
#         numeros_validos = None
#     if numeros_validos is None:
#         print('Vocẽ não digitou um ou dois números válidos. ')
#         continue

#     operadores_validos = '+-/*' #FLAG
#     if operador not in operadores_validos:
#         print('Operador inválido!')
#         continue
#     if len(operador) > 1:
#         print('Digite somente o operador escolhido. ')
#         continue

#     soma = operador == '+'
#     subtraçao = operador == '-'
#     divisao = operador == '/'
#     multiplicacao = operador == '*'
#     if soma:
#         print(f'SOMA = {numero1_float + numero2_float}')
#     elif subtraçao:
#         print(f'SUBTRAÇÃO = {numero1_float - numero2_float}')
#     elif multiplicacao:
#         print(f'MULTIPLICAÇÃO = {numero1_float * numero2_float}')
#     elif divisao:
#         if numero2_float == 0:
#             print('ERRO! Divisão por 0.')
#         else:
#             print(f'DIVISÃO = {numero1_float / numero2_float}')

#     sair = input('digite "s" para sair ou outra tecla para continuar.') \
#                                       .lower().startswith('s')
#     if sair:
#         break
