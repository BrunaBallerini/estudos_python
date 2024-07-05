import math
from array import array
from sys import getsizeof
from datetime import datetime

# nome = input("Digite o seu nome: ")
# ano_de_nascimento = input("Digite o ano que você nasceu: ")
# ano_atual = input("Qual ano estamos: ")
# idade = int(ano_atual) - int(ano_de_nascimento)
# print("Ola, {1}. Você tem {0} anos". format(idade, nome))
# if idade >= 30:
#     print("Ai senhor.")
# else:
#     print("Que bom!")

# dado = False
# print(type(dado))
# dado = 2.2
# print(type(dado))
# dado = "2.2"
# print(type(dado))
# calculo = 2**3
# print(calculo) 

# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# for row in matrix:
#     for item in row:
#         print(item)

# fruits = ["apple", "banana", "cherry"]
# colors = ["red", "yellow", "purple"]
# for fruit in fruits:
#     for color in colors:
#         print(f"{fruit} is {color}")

# for i in range(5):
#     for j in range(i + 1):
#         print(j + 1, end = ' ')
#     print()

# palavra = "FANTASTICO"
# for caractere in palavra:
#     print(caractere, end = ' ')
# print()

# matrix = [[" _", "_", "_ "], ["| ", " ", " |"], ["|_", "_", "_|"]]
# for row in matrix:
#     for item in row:
#        print(item, end = "")
#     print()

# for lado_maior in range(7):
#     # print("/", end="") -> para entender a ordem do for
#     for lado_menor in range(5):
#        print("@",end = " ")
#     print()

# valor_produto = 100
# valor_minimo = 20
# dia = 0
# estoque_inicial = 200
# while estoque_inicial > 0:
#     dia += 1
#     print( f'Dia: {dia} Valor de venda: R${valor_produto}')
#     valor_produto -= 10
#     venda_diaria = int(input("Qual foi a venda de hoje? "))
#     estoque_inicial -= venda_diaria
#     if estoque_inicial <= valor_minimo:
#         print(f'Estoque mínimo atingido no dia {dia}.')
#         break

# idade = 21
# resultado = print(f'Com {idade} anos pode votar.') if (idade >= 16) else print (f'Com {idade} anos não pode votar.') -> OPERADOR TERNARIO
# resultado = 'Voto permitido.' if idade >= 16 else 'Voto não permitido.'
# print(resultado) 

# def soma(*numeros):
#     total = 0
#     for valor in numeros:
#         total += valor
#     print(type(numeros))
#     return total
# resultado = soma(1,2,3,25)
# print(resultado)

# def agencia(**carro):
#     return carro
# nosso_carro = agencia(marca='Corolla', cor='Preto', motor='2.0')
# print(type(nosso_carro))
# print(nosso_carro)

# numero = 5  
# lista = []
# for i in range(numero, 0, -1):
#     lista.append(i)
# fatorial = 1
# for n in lista:
#     fatorial = n*fatorial
# print(fatorial)

# print(math.factorial(4))

# quant_itens = int(input('Digite a quantidade de itens que você quer na lista: '))
# lista = []
# for i in range(quant_itens):
#     item = input('Digite o item para inserir na lista: ')
#     lista.append(item)
# print(lista)

# list = ['amarelo', 'azul', 'vermelho']
# list.remove('amarelo')
# print(list)

# itens = [[1, 2], [3, 4]]
# print(itens[1][0])

# fruits = ["apple", "banana", "cherry"]
# item = []
# for fruit in fruits:
#     # for position in range(1):
#     item.append(fruit)
# print(item)

# frutas = ["maça", "banana", "abacaxi", "melancia", "uva"]
# fruta1, fruta2, *outros, fruta3 = frutas
# print(outros)

# cor_cliente = input('Digite a cor desejada: ')
# cores = ['amarelo', 'azul', 'verde', 'roxo', 'branco']
# if cor_cliente.lower() in cores:
#     print('Sim')
# else:
#     print('Não')
 
# palavra = "FANTASTICO"
# nova_palavra = []
# for caractere in palavra:
#     nova_palavra.append(caractere)
# print(nova_palavra)
# nova_palavra = list(palavra)

# cores = ['amarelo', 'azul', 'verde', 'roxo', 'branco']
# codigo = [123, 456, 789, 1011, 1213]
# nova_lista = zip(cores, codigo)
# print(list(nova_lista))

# usuario = input('Digite os itens da lista separados pos espaço: ')
# lista_usuario = usuario.split(' ') #split define o que será a separação de cada item da lista
# print(lista_usuario)

# cores = ['amarelo', 'azul', 'verde', 'roxo', 'branco']
# cores_tuple = tuple(cores)
# print(cores_tuple)

# cores = ['amarelo', 'azul', 'verde', 'roxo', 'branco']
# cores2 = ['amarelo', 'magenta', 'lilas', 'roxo', 'tuquesa']
# cores = set(cores)
# cores2 = set(cores2)
# itens_repetidos = cores & cores2
# print(itens_repetidos)
# total_cores = cores.union(cores2)
# print(total_cores)

# s = {None}
# print(type(s))

# aluno = {
#     'nome': 'Bruna', 
#     'sobrenome': 'Ballerini', 
#     'idade': '34', 
#     'nota': 9
#     }
# print(aluno['nota'])
# aluno['nome'] = 'Bru'
# aluno.update({'materias': ['Matemática', 'Física']})
# print(aluno.get('endereco', 'Não está cadastrado')) #Não gera erro caso chave e valor não estejam cadastrados
# for id, valores in aluno.items():
#     print(id, valores)
#     print(type(valores))

# def resultado(x,y):
#     soma = lambda x, y: x+y
#     return soma(x, y) * 2
# print(resultado(10,5))

# numeros = [2, 4, 6]
# def fatorial(x):
#     return math.factorial(x)
# resultado = map(fatorial,numeros)
# print(list(resultado))

# numeros = [2, 4, 6]
# fatorial = lambda x: math.factorial(x)
# resultado = map(fatorial,numeros)
#  for produto in produtos# print(list(resultado))

# numeros = [2, 4, 6]
# print(list(map(lambda x: math.factorial(x),numeros)))

# NÃO FUNCIONOU PORQUE DEPOIS DE APAGAR O PRIMEIRO ITEM MAIOR O INDICE FOI ALTERADO E SAIU DO FOR
# numeros = [10, 16, 89, 125]
# for item in numeros:
#     if item > 20:
#         numeros.remove(item)
# # print(numeros) for produto in produtos

# numeros = [10, 16, 89, 125, 255]
# def remove_maior_20(x):
#     return x > 20
# print(list(filter(remove_maior_20, numeros)))

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
#     if 'a' in fruit:
#         item.append(fruit)
# print(item) 

# fruits = ["apple", "banana", "cherry"]
# frutas = [item for item in fruits if 'a'  in item]
# print(frutas) 

# valores = [x * 10 for x in range(1000)]  
# # print(valores)
# print(getsizeof(valores))
# valores = (x * 10 for x in range(1000)) # Generator expression não armazena na memória - Altera somente o colchetes para parentesis
# # print(valores)
# print(getsizeof(valores))

# erro = 0
# while erro == 0: # Usando o break, não precisa a variável erro
#     try:
#         valor = int(input('Digite um valor: '))
#         print(valor)
#         erro += 1
#         # break # sem o break, o valor válido vai ser impresso mas nunva sairá do while porque ele é sempre true
#     except ValueError:
#         print('Digite um valor numérico. ')

# erro = 0
# somatorio = 0
# while erro == 0:
#     try:
#         valor = int(input('Digite um valor: '))
#         erro = 1
#     except ValueError:
#             print('Digite um valor numérico. ')
#     else:
#         print(f'Valor digitado: {valor}')
#     finally:
#         somatorio = somatorio +1
#         print(f'Número de tentativas: {somatorio}')

# class Funcionario:

#     def __init__(self, nome, sobrenome, nascimento, salario, funcao, email, endereco):
#         self.__nome = nome
#         self.sobrenome = sobrenome
#         self.nascimento = int(nascimento)
#         self.salario = salario
#         self.funcao = funcao
#         self.email = email
#         self.endereco = endereco
 
#     @property
#     def nome(self):
#         return self.__nome
    
#     def nome_completo(self):
#         print(f'Funcionário: {self.__nome} {self.sobrenome}')

#     def aumento_salario(self, tempo_empresa):
#         if tempo_empresa > 5:
#             self.salario += 500
#             print(f'Funcionário {self.__nome} passou a receber R$ {self.salario}.')

#     def idade(self):
#         ano_atual = datetime.now().year
#         return ano_atual - self.nascimento 


# bruna = Funcionario('Bruna', 'Ballerini', '1989', 3000, 'analista de projetos', 'brunaballerini@gmail.com', 'Juscelino Barbosa, 86')
# bruna.aumento_salario(9)
# bruna.nome_completo()
# print(bruna.idade())

#EVOLUÇÃO 1
# lista = ['a', 'b', 'b', 'd', 'e']
# base = 'b'
# for posicao, letra in enumerate(lista):
#     if letra == base:
#         print(posicao)

#EVOLUÇÃO 2
# lista = ['a', 'b', 'b', 'd', 'e']
# base = 'b'
# def find_index(to_find, item):
#     for posicao, letra in enumerate(lista):
#         if letra == base:
#             print(posicao)
#         else:
#             print('-1')
# find_index(lista, base)

#EVOLUÇÃO 3
# lista = ['a', 'b', 'b', 'd', 'e']
# base = 'b'
# def find_index(to_find, item):
#     if base in lista:
#         print(lista.index(base))
#     else: 
#         print('-1')
# find_index(lista, base)

# EXPLICAÇÃO 1:
# x = ('apple', 'banana', 'cherry')
# y = enumerate(x)
# print(list(y))

#EXPLICAÇÃO 2:
# aluno = {
#     'nome': 'Bruna', 
#     'sobrenome': 'Ballerini', 
#     'idade': '34', 
#     'nota': 9
#     }
# aluno.update({'materias': ['Matemática', 'Física']})
# for id, valores in aluno.items():
#     print(id, valores)
# print(list(aluno.items()))

# FINAL
# lista = ['a', 'b', 'b', 'd', 'e']
# base = 'w'
# indices = []
# def find_index(lista, base):
#     for posicao, letra in enumerate(lista):
#         if letra == base:
#             indices.append(posicao)
#     if indices:
#         return indices
#     else:
#         return -1
# resultado = find_index(lista, base)
# if resultado != -1:
#     print(f'O elemento "{base}" foi encontrado nas posições: {resultado}')
# else:
#     print(f'O elemento "{base}" não foi encontrado na lista.')

#FINAL MELHORADO
# lista = ['a', 'b', 'b', 'd', 'e']
# base = 'b'
# indices = []
# def find_index(lista, base):
#     indices = [posicao for posicao, letra in enumerate(lista) if letra == base]
#     if indices: #LISTA QUE CONTEM ELEMENTOS É CONSIDERADA TRUE E FALSE QUANDO VAZIA
#         return indices
#     else:
#         return -1
# resultado = find_index(lista, base)
# if resultado != -1:
#     print(f'O elemento "{base}" foi encontrado nas posições: {resultado}')
# else:
#     print(f'O elemento "{base}" não foi encontrado na lista.')