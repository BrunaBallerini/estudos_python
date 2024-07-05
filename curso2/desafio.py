import math

# temperatura = int(input('Qual a temperatura está sendo mostrada no termômetro: '))
# if temperatura <= 48:
#     print('Cozinhe mais um pouco!')
# elif 48 < temperatura <= 54:
#     print('SELADA')
# elif 54 < temperatura <= 60:
#     print('AO PONTO PARA MAL')    
# elif 60 < temperatura <= 65:
#     print('AO PONTO')
# elif 65 < temperatura <= 71:
#     print('AO PONTO PARA BEM')
# elif 71 < temperatura <= 75:
#     print('BEM PASSADA')
# else:
#    print('Retire a carne pois deve estar queimada!')

# temperatura = int(input('Qual a temperatura está sendo mostrada no termômetro: '))
# if temperatura < 48:
#     print('Cozinhe mais um pouco!')
# elif temperatura in range(48, 54):
#     print('SELADA')
# elif temperatura in range(54, 60):
#     print('AO PONTO PARA MAL')    
# elif temperatura in range(60,65):
#     print('AO PONTO')
# elif temperatura in range(65, 71):
#     print('AO PONTO PARA BEM')
# elif temperatura in range(71,75):
#     print('BEM PASSADA')
# else:
#    print('Retire a carne pois deve estar queimada!')

# def calculadora_latas_tinta():

#     largura_parede = input('Largura: ')
#     altura_parede = input('Altura: ')
#     rendimento = input('Rendimento da tinta: ')
    
#     try:
            
#         largura_parede_tratada = float(largura_parede.replace(',', '.'))
#         altura_parede_tratada = float(altura_parede.replace(',', '.'))
#         rendimento_tratado = float(rendimento.replace(',', '.'))

#         area_parede = largura_parede_tratada * altura_parede_tratada
#         quant_latas = math.ceil(area_parede / rendimento_tratado)
#         print(f'Quantidade de latas: {quant_latas}')
#     except ValueError:
#         print('Favor digitar os números com separação em "." ')

# calculadora_latas_tinta()

# funcionarios = ['Ana', 'Marcos', 'Alice', 'Pedro', 'Sophia', 'Bruno', 'Melissa']
# turno_dia = ['Ana', 'Marcos', 'Alice', 'Melissa']
# turno_noite = ['Pedro', 'Sophia', 'Bruno']
# tem_carro = ['Marcos', 'Alice', 'Bruno', 'Melissa']
# noite_carro = list(set(turno_noite).intersection(set(tem_carro)))
# dia_carro = list(set(turno_dia).intersection(set(tem_carro)))
# nao_tem_carro = list(set(funcionarios).difference(set(tem_carro)))
# print('Funcionários que trabalham a noite e tem carro', end=': ')
# for nomes in noite_carro:
#     print(nomes, end=' ')
# print()
# print('Funcionários que trabalham de dia e tem carro', end=': ')
# for nomes in dia_carro:
#     print(nomes, end = ' ')
# print()
# print('Funcionários que não tem carro', end=': ')
# for nomes in nao_tem_carro:
#     print(nomes, end = ' ')
# print()

# nome = input('Digite o seu nome: ')
# altura = input('Digite a sua altura em cm: ')
# peso = input('Digite o seu peso em kg: ')
# peso_str = peso.replace(',', '.')
# altura_str = altura.replace(',', '.')
# imc = float(peso_str) / ((float(altura_str) / 100) ** 2)
# # print('IMC = {:.2f}'. format(imc))
# print(f'IMC = {imc:.2f}')
# if imc < 18.5:
#     print(f'{nome} está magra')
# elif 18.5 <= imc < 25.0:
#     print(f'{nome} está normal')
# elif 25.0 <= imc < 30.0:
#     print(f'{nome} esta com sobrepeso')
# elif 30.0 <= imc < 40.0:
#     print(f'{nome} esta com obesidade') 
# else:
#     print(f'{nome} esta com obesidade grave')

# first_name = input('Qual o seu nome: ')
# age = input('E a sua idade: ')
# print(f'O seu nome é {first_name} e a sua idade é {age}.')

# numero1 = float(input('Digite o primeiro número: '))
# numero2 = float(input('Digite o segundo número: '))
# adicao = numero1 + numero2
# subtracao = numero1 - numero2
# divisao = numero1 / numero2
# multiplicacao = numero1 * numero2
# exponenciacao = numero1 ** numero2
# print('ADIÇÃO: {:.3f} \nSUBTRAÇÃO: {:.3f} \nDIVISÃO: {:.3f} \nMULTIPLICAÇÃO: {:.3f} \nEXPONENCIAÇÃO: {:.3f}'. format(adicao, subtracao, divisao, multiplicacao, exponenciacao))

# lista = []
# tamanho = int(input('Qual o tamanho da lista: '))
# for n in range (0, tamanho):
#     item = input('Digite o item {0} da lista: '. format (n))
#     lista.append(item)
# print(lista[0], lista[(-1)])

# i=0
# frutas = ["maça", "banana", "pera", "manga"]
# for n in frutas:
#     i+=1
# print(frutas[0], frutas[i-1])
# frutas = ["maça", "banana", "pera", "manga"]
# print(frutas[0], frutas[-1])

# frutas = ["maça", "banana", "manga", "uva"]
# frutas[1] = 'morango'
# frutas.append('abacaxi')
# frutas.remove('manga')
# del(frutas[-1])
# print(frutas)
# for fruta in frutas:
#     print('Eu gosto de: {0}'. format(fruta))

# for i in range (1, 11):
#     print(i)

# frutas = ["maça", "banana", "manga", "uva"]
# legumes = ["abobrinha", "berinjela", "tomate", "brocolis"]
# for fruta in frutas:
#     for legume in legumes:
#         print(f'{fruta} - {legume}')

# i=0
# while i < 10:
#     i+=1
#     if i == 5:
#         break
#     print(i)

# for i in range(1,11,1):
#     if i == 5:
#         continue
#     print(i)

# i=0
# frutas = ["maça", "banana", "manga", "uva", "abacaxi", "maça", "ameixa", "maça"]
# for fruta in frutas:
#     if fruta == "maça":
#         i+=1
# print(f'Maça aparece: {i} vezes.')

# numero = float(input('Digite um número: '))
# if numero <= 10.0: 
#     print('O número é menor ou igual que 10.')
# elif numero > 10.0:
#     print('O número é maior que 10.')

# idade = int(input('Digite sua idade: '))
# if idade < 13: 
#     print('CRIANÇA')
# elif idade >= 13 and idade <= 19:
#     print('ADOLESCENTE')
# else:
#     print('ADULTO')

# carros_estoque = ['BMW X6', 'BMW I5', 'BMW I8']
# carro_desejado = input('Digite o modelo do carro que você gostaria de comprar: ')
# if carro_desejado.upper() in carros_estoque:
#     print(f'Carro {carro_desejado.upper()} no estoque.')
# else:
#     print('Carro não esta em estoque. ')

# fruits = ["apple", "banana", "cherry"]
# item = []
# for fruit in fruits:
#     for letra in fruit:
#         if letra == 'b':
#             item.append(fruit)
# print(item) 

# fruits = ["apple", "banana", "cherry"]
# item = []
# for fruit in fruits:
#     if 'b' in fruit:
#         item.append(fruit)
# print(item) 

# fruta = input('Digite o nome da fruta: ').lower()
# while fruta != 'abacate':
#     print('Você nao acertou. Tente novamente.')
#     fruta = input('Digite o nome da fruta: ')
# print('Parabens! Você acertou. ')

# while True:
#     fruta = input('Digite o nome da fruta: ').lower().strip()
#     if fruta == 'abacate':
#         print('Parabens! Você acertou.')
#         break
#     else:
#         print('Você não acertou. Tente novamente.')

# for i in range (0, 11):
#     if i % 2 == 0:
#         print(f'O número {i} é par.')
#     else: 
#         print(f'O número {i} é ímpar.')

# lista = list(range(1,11))
# print(lista)

# cidades = ('são paulo', 'rio de janeiro', 'salvador')
# cidade = input('Digite o nome da cidade: ').lower()
# if cidade in cidades:
#     print('A cidade está na lista.')
# else:
#     print('A cidade não está na lista. ')

# paises = ['BRASIL', 'EUA', 'INGLATERRA', 'ALEMANHA']
# capitais = ['BRASÍLIA', 'WASHINGTON', 'LONDRES', 'BERLIN']
# paises_capitais = dict(zip(paises, capitais))
# pais_escolhido = input('Digite um pais: ').upper()
# for pais, capital in paises_capitais.items():
#     if pais_escolhido == pais:
#         print(f'{pais} - {capital}')

# paises = ['BRASIL', 'EUA', 'INGLATERRA', 'ALEMANHA']
# capitais = ['BRASÍLIA', 'WASHINGTON', 'LONDRES', 'BERLIN']
# paises_capitais = dict(zip(paises, capitais))
# pais_escolhido = input('Digite um pais: ').upper()
# if pais_escolhido in paises_capitais.keys():
#     print (f'{pais_escolhido} - {paises_capitais[pais_escolhido]}')
# else:
#     print('Não temos informação sobre este país. ')

# amigos1 = {'patricia', 'juliana', 'neide', 'marilene', 'marcelo'}
# amigos2 = {'marcelo', 'jose paulo', 'neide', 'antonio', 'francisco'}
# print(amigos1.intersection(amigos2))
# print(amigos1.difference(amigos2))
# print(amigos2.difference(amigos1))
# print(amigos1.union(amigos2))

# def quadrado_numero(numero):
#     return numero ** 2
# numero = float(input('Digite o número para ser elevado ao quadrado: '))
# print(f'O resultado é {quadrado_numero(numero)}')

# def soma(numero1, numero2):
#     return numero1 + numero2
# numero1 = float(input('Digite o primeiro número a ser somado: '))
# numero2 = float(input('Digite o segundo número a ser somado: '))
# print(f'O resultado é {soma(numero1, numero2)}')

# def exponenciação(base, expoente = 2):
#     return base ** expoente
# numero_base = float(input('Digite a base: '))
# numero_expoente = input('Digite o exponente (defalut = 2): ')
# if numero_expoente:
#     print(f'O resultado é {exponenciação(numero_base, float(numero_expoente))}')
# else:
#     print(f'O resultado é {exponenciação(numero_base)}')

# def factorial(number):
#     factorial = 1
#     for n in range (1, number+1):
#         factorial = factorial * n
#     return factorial
# number = int(input('Enter a number: '))
# result = factorial(number)
# formatted_number = f'{result:,}'
# formatted_number = formatted_number.replace(',', '.')
# print(f'The factorial of the {number} is {formatted_number}')

#EXPLICAÇÃO
# numero = 1234567  # Substitua pelo número que deseja formatar
# # Use a f-string para formatar o número com separadores de milhares
# formatted_numero = f'{numero:,}'
# # Imprima o valor formatado
# print(f'O número formatado é {formatted_numero}')

# def fatorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * fatorial(n-1)s
# print(fatorial(4))

# def multiplica_2(numero):
#     return numero * 2
# def quadrado_dobro(numero):
#     return multiplica_2(numero) ** 2
# numero = float(input('Digite um numero: '))
# print(f'X: {numero} - 2X: {multiplica_2(numero)} - (2X)²: {quadrado_dobro(numero)}')

# multiplica_2 = lambda numero: numero * 2
# quadrado_dobro = lambda numero: multiplica_2(numero) ** 2
# numero = float(input('Digite um numero: '))
# print(f'X: {numero} - 2X: {multiplica_2(numero)} - (2X)²: {quadrado_dobro(numero)}')

# cubo = lambda x: x ** 3
# number = float(input('Enter a number: '))
# print(cubo(number))

# multiplica = lambda number1, number2: number1 * number2
# x = float(input('Digite um numero: '))
# y = float(input('Digite outro numero: '))
# print(f'{x} X {y} = {multiplica(x, y)}')

# par_impar = lambda x: 'par' if x % 2 == 0 else 'impar'
# numero = int(input('Digite um número: '))
# print(f'{numero} é {par_impar(numero)}')

# def matematica(numero):
#     return numero ** 2
# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# resultados = []
# for numero in numeros:
#     q = matematica(numero)
#     resultados.append(q)
# print(resultados)

# matematica = lambda numero: numero ** 2
# quant = int(input('Digite o tamanho da lista: '))
# numeros = []
# for x in range (quant):
#     valor = int(input(f'Digite o {x+1}° valor: '))
#     numeros.append(valor)
# resultados = []
# for numero in numeros: 
#     resultados.append(matematica(numero))
# print(resultados)