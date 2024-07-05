# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=invalid-name

# https://docs.python.org/3/library/re.html
# https://docs.python.org/3/howto/regex.html#regex-howto

# Funções search, findall, sub, compile
# import re
# string = 'Este é um teste de expressões regulares. Este é outro teste'
# print(re.search(r'teste', string))
# print(re.findall(r'teste', string))
# print(re.sub(r'teste', 'substituto', string, count=1))

# regexp = re.compile(r'teste')
# print(regexp.search(string))
# print(regexp.findall(string))
# print(regexp.sub('substituto', string))

# _________________________________________________________________________#

# Meta caracteres: . ^ $ * + ? { } [ ] \ | ( )
# | OU
# . Qualquer caractere (com exceção da quebra de linha)
# [] conjunto de caracteres

# import re

# texto = '''
# João trouxe    flores para sua amada namorada em 10 de janeiro de 1970,
# Maria era o nome dela.


# Foi um ano excelente na vida de joão. Teve 5 filhos, todos adultos atualmente
# maria, hoje sua esposa, ainda faz aquele café com pão de queijo nas tardes de
# domingo. Também né! Sendo a boa mineira que é, nunca esquece seu famoso
# pão de queijo.
# Não canso de ouvir a Maria:
# "Joooooooooãooooooo, o café tá prontinho aqui. Veeemm"!
# '''
# # print(re.findall(r'[Jj]oão|[Mm]aria| o |v.da', texto))
# print(re.findall(r'[a-zA-z0-9]aria', texto))
# print(re.findall(r'joão|maria', texto, flags=re.IGNORECASE))
# print(re.findall(r'joão|maria', texto, flags=re.I))

# _________________________________________________________________________#

# Meta caracteres: ^ $ ( ) -> Quantificadores
# * 0 ou n
# + 1 ou n {1,}
# ? 0 ou 1
# {n}
# {min, max}
# {10,} 10 ou mais
# {,10} De zero a 10
# {10} Especificamente 10
# {5,10} De 5 a 10
# ()+ [a-zA-Z0-9]+


# import re

# texto = '''
# João trouxe    flores para sua amada namorada em 10 de janeiro de 1970,
# Maria era o nome dela.


# Foi um ano excelente na vida de joão. Teve 5 filhos, todos adultos atualmente
# maria, hoje sua esposa, ainda faz aquele café com pão de queijo nas tardes de
# domingo. Também né! Sendo a boa mineira que é, nunca esquece seu famoso
# pão de queijo.
# Não canso de ouvir a Maria:
# "Joooooooooãooooooo, o café tá prontinho aqui. Veeemm"!
# jooão
# Jão
# '''
# print(re.findall(r'Jo+ão+', texto, flags=re.I))
# print(re.findall(r'Jo*ão', texto, flags=re.I))
# print(re.findall(r'Jo{1,2}ão', texto, flags=re.I))
# print(re.findall(r've{3}m{1,2}', texto, flags=re.I))

# texto2 = 'João ama ser amado'
# print(re.findall(r'ama[od]{0,2}', texto2, flags=re.I))

# _________________________________________________________________________#

# Meta caracteres: ^ $ ( )
# * 0 ou n
# + 1 ou n -> pesquisa gulosa
# ? 0 ou 1 -> pesquisa não gulosa

# import re

# texto = '''
# <p>Frase 1</p> <p>Eita</p> <p>Qualquer frase</p> <div>1</div>
# '''

# print(re.findall(r'<[dpiv]{1,3}>', texto))
# print(re.findall(r'<[dpiv]{1,3}>.+<\/[dpiv]{1,3}>', texto))
# print(re.findall(r'<[dpiv]{1,3}>.+?<\/[dpiv]{1,3}>', texto))

# _________________________________________________________________________#

# Meta caracteres: ^ $
# ()     \1
# () ()  \1 \2
# (()) ()   \1 \2 \3
# ?: Encontra o que vem a seguir mas não salva ->
# import re
# from pprint import pprint

# cpf = 'a 147.852.963-12 a'
# print(re.findall(r'((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})', cpf))

# texto = '''
# <p>Frase 1</p> <p>Eita</p> <p>Qualquer frase</p> <div>1</div>
# '''
# tags = re.findall(r'<(([dpiv]{1,3})>.+?<\/\2>)', texto)
# tags = re.findall(r'(<([dpiv]{1,3})>(.+?)<\/\2>)', texto)
# for tag in tags:
#     um, dois, tres = tag
#     print(um)
#     print(tres)

# tags = re.findall(r'<([dpiv]{1,3})>(.+?)<\/\1>', texto)
# tags = re.findall(r'<(?P<tag>[dpiv]{1,3})>(.+?)<\/(?P=tag)>', texto)
# pprint(tags)

# print(re.sub(r'(<(.+?)>)(.+?)(<\/\2>)', r'\1 MAIS \3 COISAS \4', texto))

# _________________________________________________________________________#

# Meta caracteres:
# ^ -> começa com
# $ -> termina com
# [^a-z] -> Negação

# import re

# cpf = '147.852.963-12'
# print(re.findall(r'^((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})$', cpf))
# print(re.findall(r'[^0-9]+', cpf))
# print(re.findall(r'[^a-zA-Z]+', cpf))

# _________________________________________________________________________#

# \w -> [a-zA-Z0-9À-ú_]
# \w -> [a-zA-Z0-9_] -> re.A
# \W -> [^a-zA-Z0-9À-ú_]
# \W -> [^a-zA-Z0-9_] -> re.A
# \d -> [0-9]
# \D -> [^0-9]
# \s -> [ \r\n\f\v\t] -> espaços e tabulação
# \S -> [^ \r\n\f\v\t]
# \b -> borda
# \B -> não borda

# import re

# texto = '''
# João trouxe    flores para sua amada namorada em 10 de janeiro de 1970,
# Maria era o nome dela.
# Foi um ano excelente na vida de joão. Teve_ALGO 5 filhos, todos adultos
# atualmente. maria, hoje sua esposa, ainda faz aquele café com pão de queijo
# nas tardes de domingo. Também né! Sendo a boa mineira que é, nunca esquece
# seu famoso pão de queijo. Não canso de ouvir a Maria:
# "Joooooooooãooooooo, o café tá prontinho aqui. Veeemm"!
# '''
# print(re.findall(r'[a-z]+', texto, flags=re.I))
# print(re.findall(r'[a-zA-Z]+', texto))
# print(re.findall(r'[a-zA-Z0-9]+', texto))
# print(re.findall(r'\w+', texto, flags=re.A))
# print(re.findall(r'[a-zA-Z0-9À-ú]+', texto))
# print(re.findall(r'\w+', texto, flags=re.I))
# print(re.findall(r'\W+', texto, flags=re.I))
# print(re.findall(r'\W+', texto, flags=re.A))
# print(re.findall(r'\d+', texto, flags=re.I))
# print(re.findall(r'\D+', texto, flags=re.I))
# print(re.findall(r'\s+', texto, flags=re.I))
# print(re.findall(r'\S+', texto, flags=re.I))
# print(re.findall(r'\bf\w+', texto, flags=re.I))
# print(re.findall(r'\w+s\b', texto, flags=re.I))
# print(re.findall(r'\b\w{4}\b', texto, flags=re.I))
# print(re.findall(r'\w{4}', texto, flags=re.I))
# print(re.findall(r'flo\B', texto, flags=re.I))

# _________________________________________________________________________#


# re.A -> ASCII
# re.I -> IGNORECASE
# re.M -> Multiline -> ^ $
# re.S -> Dotall \n
# import re

# texto = '''
# 131.768.460-53 ABC
# 055.123.060-50 DEF
# 955.123.060-90
# '''

# print(re.findall(r'\d{3}\.\d{3}\.\d{3}\-\d{2}', texto))
# print(re.findall(r'^\d{3}\.\d{3}\.\d{3}\-\d{2}$', texto, flags=re.M))

# texto2 = '''O João gosta de folia
# E adora ser amado'''
# print(re.findall(r'^o.*o$', texto2, flags=re.I | re.S))

# _________________________________________________________________________#

# import re
# from pprint import pprint

# texto = '''
# ONLINE  192.168.0.1 GHIJK active
# OFFLINE  192.168.0.2 GHIJK inactive
# OFFLINE  192.168.0.3 GHIJK active
# ONLINE  192.168.0.4 GHIJK active
# ONLINE  192.168.0.5 GHIJK inactive
# OFFLINE  192.168.0.6 GHIJK active
# '''

# Positive lookahead
# pprint(re.findall(r'\w+\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+(?=active)', texto))

# Negative lookahead
# pprint(re.findall(r'\w+\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+(?!active)', texto))

# Positive lookahead
# pprint(re.findall(r'(?=.*[^in]active).+', texto))

# Positive lookbehind
# pprint(
#     re.findall(r'\w+(?<=ONLINE)\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+\w+', texto)
# )

# Negative lookbehind
# pprint(
#     re.findall(r'\w+(?<!ONLINE)\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+\w+', texto)
# )

# Positive lookbehind
# pprint(
#     re.findall(r'\w+(?<=OFFLINE)\s+\d+\.\d+\.\d+\.\d+\s+\w+\s+\w+', texto)
# )
# Negative lookbehind
# pprint(
#     re.findall(r'\w+(?<!OFFLINE)\s+\d+\.\d+\.\d+\.\d+\s+\w+\s+\w+', texto)
# )

# _________________________________________________________________________#

# import re

# 0.0.0.0 255.255.255.255
# 025.258.963-10 02525896310

# Teste essa expressão
# em https://regex101.com/r/lWVPOr/1
# cpf = '025.258.963-10'
# cpf_reg_exp = re.compile(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$', flags=0)
# print(cpf_reg_exp.search(cpf))

# Teste essa expressão
# em https://regex101.com/r/XDyL7q/1
# ip_reg_exp = re.compile(
#     r'^'  # Começa com
#     r'(?:'
#     r'(?:25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9][0-9]|[0-9])\.'
#     r'){3}'  # Sequência de 3 digitos e um ponto repete 3x
#     r'(?:25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9][0-9]|[0-9])'
#     r'$',  # Termina com
#     flags=0
# )

# for i in range(301):
#     ip = f'{i}.{i}.{i}.{i}'

#     print(ip, ip_reg_exp.findall(ip))


# test = re.compile(r'^(?:\d{3}-){2}\d{4}$')
# for i in range(100, 110):
#     c = f'{i}-{i}-{i}0'
#     print(c, test.findall(c))

# _________________________________________________________________________#

# https://regex101.com/r/0OM1oz/1/

# import re
# from pprint import pprint

# regex = re.compile(
#     r"^(?!(\d)\1{2}\.\1{3}\.\1{3}-\1{2})(\d{3}\.\d{3}\.\d{3}-\d{2})$",
#     flags=re.MULTILINE
# )

# test_str = ("698.547.520-54\n"
#             "060.235.190-16\n"
#             "683.134.960-96\n"
#             "899.344.730-62\n"
#             "103.778.870-21\n"
#             "721.478.580-30\n"
#             "366.310.090-14\n"
#             "794.289.350-26\n"
#             "190.259.410-01\n"
#             "000.000.000-01\n"
#             "900.000.000-00\n\n"
#             "000.000.000-00\n"
#             "111.111.111-11\n"
#             "222.222.222-22\n"
#             "333.333.333-33\n"
#             "444.444.444-44\n"
#             "555.555.555-55\n"
#             "666.666.666-66\n"
#             "777.777.777-77\n"
#             "888.888.888-88\n"
#             "999.999.999-99\n\n"
#             )

# pprint(regex.findall(test_str))

# _________________________________________________________________________#

# import re

# https://regex101.com/r/DfXYXM/1/
# regexp = re.compile(
#     r'^(?:\(\d{2}\)\s*)?(?:9\s)?(?:\d{4}-\d{4})$', flags=re.M
# )

# texto = '''
# (21) 9 8852-5214
# (11)9955-1231
# (11)  9955-1231
# (35) 9 9975-4521
# (31) 3851-2587
# 9 8571-5213
# 1234-5647
# '''

# for telefone in regexp.findall(texto):
#     print(telefone)

# _________________________________________________________________________#


# import re

# https://regex101.com/r/W4kRV2/2/
# https://en.wikipedia.org/wiki/List_of_Unicode_characters

# senha_forte_regexp = re.compile(
#     r'^'
#     r'(?=.*[a-z])'
#     r'(?=.*[A-Z])'
#     r'(?=.*[0-9])'
#     r'(?=.*[ -\/:-@[-`{-~])'
#     r'.{12,}'
#     r'$',
#     flags=re.M
# )

# string = '''
# VÁLIDAS
# v2Ts7<o9T~}Y
# j25TTbjJ:6{<
# s`Mu6T;4M1!y
# Li`hk6:3WX>3
# d.D09}^dI2Vn

# SEM MINÚSCULAS
# I7^Y3RS^ 9]7
# [P6W"83L5V{[
# B7=;K8D6_}W5
# 1B_RT`93R%>1
# EZU{7;2&D:64

# SEM MINÚSCULAS E NÚMEROS
# E}LV`C?X_G:{
# AJH[@HD*V~=<
# *A~AC{_V~MG-
# W<-T}W:QAF'{
# ~YJ}|FILN>~)

# SEM NÚMEROS CARACTERES E MINÚSCULAS
# PBDZDPECUDNN
# EJQWFWFFDEHY
# XRCNLNRHYOZJ
# TWIYPLWUDMNN
# JMDTJSEPKVON

# QUANTIDADE INVÁLIDA (6)
# Iu4<1j
# 1x`P6g
# @9t3Ry
# qf9_6H
# 0o`9fO
# '''

# print(senha_forte_regexp.findall(string))


# from random import choice, randint, shuffle
# def zero_a_nove():
#     return chr(randint(48, 57))


# def a_a_z():
#     return chr(randint(97, 122))


# def A_a_Z():
#     return chr(randint(65, 90))


# def strange_chars():
#     rand_range = [
#         randint(32, 47),  # \u0020-\u002F [ -\/]
#         randint(58, 64),  # \u003A-\u0040 [:-@]
#         randint(91, 96),  # \u005B-\u0060 [[-`]
#         randint(123, 126),  # \u007B-\u007E [{-~]
#     ]

# [\u0020-\u002F\u003A-\u0040\u005B-\u0060\u007B-\u007E]
# [ -\/:-@[-`{-~]

#     return chr(choice(rand_range))


# def create_pass(
#         length=12,
#         upper=True,
#         lower=True,
#         numbers=True,
#         chars=True
# ):
#     password = []

#     for _ in range(length):
#         if numbers:
#             password.append(zero_a_nove())
#         if lower:
#             password.append(a_a_z())
#         if upper:
#             password.append(A_a_Z())
#         if chars:
#             password.append(strange_chars())

#     password = password[:length]
#     shuffle(password)
#     return ''.join(password)


# if __name__ == '__main__':

#     print('VÁLIDAS')
#     for i in range(5):
#         print(create_pass(
#             length=12,
#             chars=True,
#             upper=True,
#             lower=True,
#             numbers=True
#         ))
#     print()

#     print('SEM MINÚSCULAS')
#     for i in range(5):
#         print(create_pass(
#             length=12,
#             chars=True,
#             upper=True,
#             lower=False,
#             numbers=True
#         ))
#     print()

#     print('SEM MINÚSCULAS E NÚMEROS')
#     for i in range(5):
#         print(create_pass(
#             length=12,
#             chars=True,
#             upper=True,
#             lower=False,
#             numbers=False
#         ))
#     print()

#     print('SEM NÚMEROS CARACTERES E MINÚSCULAS')
#     for i in range(5):
#         print(create_pass(
#             length=12,
#             chars=False,
#             upper=True,
#             lower=False,
#             numbers=False
#         ))
#     print()

#     print('QUANTIDADE INVÁLIDA (6)')
#     for i in range(5):
#         print(create_pass(
#             length=6,
#         ))
#     print()


# _________________________________________________________________________#

# https://regex101.com/r/wjfSus/1/

# import re

# text = '''
# Válidos
# 0.0
# 00.00
# 000.000
# +0.0
# -00.00
# +000.000
# 10
# 50
# 8.5
# -8.5
# +10.5005412136
# 1231345458.54654564
# -133215646589.6543215648978977
# +1.11123123
# -0.154987
# 1.121654987
# 10.123
# 10.1
# -1.1

# Inválidos
# 10..2
# ++1213
# --1235050
# .124546
# -.1231324
# 10.
# .1
# .10
# 10.
# +10.
# -10.
# 5a
# b5
# '''


# def is_float(string) -> bool:
#     return bool(re.search(r'^[+-]?\d+(?:\.\d+)?$', string))


# def is_int(string) -> bool:
#     return bool(re.search(r'^[+-]?\d+$', string))


# while True:
#     numero = input('Digite um número: ')

#     if is_int(numero):
#         numero = int(numero)  # type: ignore
#         print(f'O número {numero} foi convertido para int')
#         continue

#     if is_float(numero):
#         numero = float(numero)  # type: ignore
#         print(f'O número {numero} foi convertido para float')
#         continue

# _________________________________________________________________________#

# """
# Básica
# ^\w+(?:[.\-+!%]\w+)*@\w+(?:[.\-]\w+)+$
# https://regex101.com/r/9s4bgv/1/

# Básica 2
# ^[^\s@<>\(\)[\]\.]+(?:\.[^\s@<>\(\)\[\]\.]+)*@\w+(?:[\.\-_]\w+)*$
# https://regex101.com/r/mH4ChC/2/

# rfc 5322
# ^(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])$
# https://regex101.com/r/fkxI15/1/
# """

# emails = """
# Valid email addresses
# o-que_vai.te+dar+dor-de.cabeca@gmail-com-traco.com.br
# simple@example.com
# very.common@example.com
# disposable.style.email.with+symbol@example.com
# other.email-with-hyphen@example.com
# fully-qualified-domain@example.com
# user.name+tag+sorting@example.com
# x@example.com
# example-indeed@strange-example.com
# example@s.example
# a@a.com.br
# mailhost!username@example.org
# user%example.com@example.org
# email@example.com
# firstname.lastname@example.com
# email@subdomain.example.com
# firstname+lastname@example.com
# email@123.123.123.123
# "email"@example.com
# 1234567890@example.com
# email@example-one.com
# _______@example.com
# email@example.name
# email@example.museum
# email@example.co.jp
# firstname-lastname@example.com


# Invalid email addresses
# Abc.example.com
# <aqui-te-um@email-pra-validar.com.br>
# A@b@c@example.com
# a"b(c)d,e:f;g<h>i[j\k]l@example.com
# just"not"right@example.com
# this is"not\allowed@example.com
# this\ still\"not\\allowed@example.com
# plainaddress
# #@%^%#$@#$@#.com
# @example.com
# <email@example.com>
# email.example.com
# email@example@example.com
# .email@example.com
# email.@example.com
# email..email@example.com
# あいうえお@example.com
# email@example
# email@-example.com
# email@example..com
# Abc..123@example.com
# ”(),:;<>[\]@example.com
# just”not”right@example.com
# this\ is"really"not\allowed@example.com
# """
