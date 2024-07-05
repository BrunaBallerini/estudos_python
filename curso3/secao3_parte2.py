# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# type: ignore

# import os
# string = 'FREDERICO :)'
# indice = 0
# tamanho_string = len(string)
# while indice < tamanho_string:
#     letra = string[indice]

#     if letra == ' ':
#         break

#     print(letra, end = ' ')
#     indice += 1
# else:
#     print('Strng não tem espaço. ')
# Se o while for executado, o else também executa. Se ele sair por um break,
# por exemplo, ele não executa

# frase = 'Se você não pode mudar seu destino, mude sua atitude.'.lower()
# letra_procurada = 's'
# contador = 0
# for letra in frase:
#     if letra == letra_procurada:
#         contador += 1
# print(contador)

# frase = 'Eu só acordo mais cedo para poder me atrasar com calma'.lower()
# letra_procurada = 'c'
# tamanho_frase = len(frase)
# indice = 0
# contador = 0
# while indice < tamanho_frase:
#     letra_atual = frase[indice]
#     if letra_atual == letra_procurada:
#         contador += 1
#     indice +=1
# print(f'Tem {contador} letras "{letra_procurada}" na frase: {frase}')

# frase = 'Eu só acordo mais cedo para poder me atrasar com calma'.lower()
# tamanho_frase = len(frase)
# indice = 0
# quant_mais_vezes = 0
# letra_mais_vezes = ''
# while indice < tamanho_frase:
#     letra_atual = frase[indice]
#     if letra_atual == ' ':
#         indice +=1
#         continue
#     quant_atual = frase.count(letra_atual)
#     if quant_atual > quant_mais_vezes:
#         quant_mais_vezes = quant_atual
#         letra_mais_vezes = letra_atual
#     indice +=1
# print(f'{letra_mais_vezes} - {quant_mais_vezes}')

# FORMA DE RESOLVER
# frase = 'Eu só acordo mais cedo para poder me atrasar com calma'.lower()
# contagem_letras = {}
# for letra in frase:
# Certifique-se de que a letra seja uma letra do alfabeto
#     if letra.isalpha():
#         if letra in contagem_letras:
#             contagem_letras[letra] += 1
#         else:
#             contagem_letras[letra] = 1
# chave_mais_frequente = max(contagem_letras, key=contagem_letras.get)
# contagem_mais_frequente = contagem_letras[chave_mais_frequente]
# print(f'A letra mais frequente é "{chave_mais_frequente}"')
# print(f'com {contagem_mais_frequente} ocorrências.')

# EXPLICAÇÃO 1
# dicionario = {}
# palavra = 'PALAVRA'
# for letra in palavra:
#     if letra in dicionario:
#         dicionario[letra] += 1
#     elif letra not in dicionario:
#         dicionario[letra] = 1
# print(dicionario)
# EXPLICAÇÃO 2
# dicionario = {'B':1, 'A':3, 'N':2}
# maximo = max(dicionario, key = dicionario.get)
# print(maximo)

# palavra = "FANTASTICO"
# nova_palavra = []
# for caractere in palavra:
#     nova_palavra.append(caractere)
# print(nova_palavra)
# nova_palavra = list(palavra)

# palavra = "FANTASTICO"
# nova_palavra = ''
# for caractere in palavra:
#     nova_palavra += f' {caractere}'
# print(nova_palavra)

# numeros = range(0,100, 8)
# print('Multiplos de 8:')
# for numero in numeros:
#     print(numero, end='-')

# tentativas = 0
# palavra_base = list('banana')

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

# EXPLICAÇÃO:
# palavra = "BANANA"
# letra = 'A'
# nova_palavra = ''
# for caractere in palavra:
#     if caractere == letra:
#         nova_palavra += f' {caractere}'
# print(nova_palavra)
