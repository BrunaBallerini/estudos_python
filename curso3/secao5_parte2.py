# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# type: ignore

# super() e a sobreposição de membros
# Classe principal
#   -> super class, base class, parent class
# Classes filhas
#   -> sub class, child class, derived class
# class MinhaString(str):
#     def upper(self):
#         print('CHAMOU UPPER')
#         retorno = super(MinhaString, self).upper()
#         print('DEPOIS DO UPPER')
#         return retorno

# string = MinhaString('Luiz')
# print(string.upper())

# class A(object):
#     atributo_a = 'valor a'
#     def __init__(self, atributo):
#         self.atributo = atributo

#     def metodo(self):
#         print('A')

# class B(A):
#     atributo_b = 'valor b'
#     def __init__(self, atributo, outra_coisa):
#         super().__init__(atributo)
#         self.outra_coisa = outra_coisa

#     def metodo(self):
#         print('B')

# class C(B):
#     atributo_c = 'valor c'
#     def __init__(self, *args, **kwargs):
#         # print('EI, burlei o sistema.')
#         super().__init__(*args, **kwargs)

#     def metodo(self):
#         # super().metodo()  # B
#         # super(B, self).metodo()  # A
#         # super(A, self).metodo()  # object
#         A.metodo(self)
#         B.metodo(self)
#         print('C')

# # print(C.mro()) # RETORNA O METHOD RESOLUTION ORDER
# # print(B.mro())
# # print(A.mro())
# c = C('Atributo', 'Qualquer')
# # print(c.atributo)
# # print(c.outra_coisa)
# c.metodo()
# # print(c.atributo_a)
# # print(c.atributo_b)
# # print(c.atributo_c)
# # c.metodo()

# ABSTRACT BASE CLASS
# from abc import ABC, ABCMeta, abstractmethod
# from pathlib import Path
# import json

# LOG_FILE = Path(__file__).parent / 'log.txt'
# # class Log(metaclass=ABCMeta):
# #     pass

# class Log(ABC):
#     @abstractmethod
#     def _log(self, msg): # MÉTODO ABSTRATO
#         pass

#     def log_error(self, msg):
#         return self._log(f'ERROR: {msg}')

#     def log_success(self, msg):
#         return self._log(f'SUCCESS: {msg}')

# class LogFileMixin(Log):
#     def _log(self, msg):
#         msg_formated = f'{msg} - {self.__class__.__name__}'
#         with open(LOG_FILE, 'a') as arquivo:
#             arquivo.write(msg_formated)
#             arquivo.write('\n')

# class LogPrintMixin(Log):
#     def _log(self, msg):
#         print(f'{msg} - {self.__class__.__name__}')

# l = LogPrintMixin()
# l.log_success('success')

# abstractmethod para qualquer método já decorado (@property e setter)
# É possível criar @property @property.setter @classmethod
# @staticmethod e métodos normais como abstratos, para isso
# use @abstractmethod como decorator mais interno.
# Foo - Bar são palavras usadas como placeholder
# para palavras que podem mudar na programação.
# from abc import ABC, abstractmethod

# class AbstractFoo(ABC):
#     def __init__(self, name):
#         self._name = name
#         # self.name = name

#     @property
#     def name(self):
#         return self._name

#     @name.setter
#     @abstractmethod
#     def name(self, name): ...

# class Foo(AbstractFoo):
#     def __init__(self, name):
#         super().__init__(name)

#     @AbstractFoo.name.setter
#     def name(self, name):
#         self._name = name

# foo = Foo('Bar')
# print(foo.name)

# Polimorfismo em Python Orientado a Objetos
# Polimorfismo é o princípio que permite que
# classes deridavas de uma mesma superclasse
# tenham métodos iguais (com mesma assinatura)
# mas comportamentos diferentes.
# Assinatura do método = Mesmo nome e quantidade
# de parâmetros (retorno não faz parte da assinatura)
# Opinião + princípios que contam:
# Assinatura do método: nome, parâmetros e retorno iguais
# SO"L"ID
# Princípio da substituição de liskov
# Objetos de uma superclasse devem ser substituíveis
# por objetos de uma subclasse sem quebrar a aplicação.
# Sobrecarga de métodos (overload)  🐍 = ❌
# Sobreposição de métodos (override) 🐍 = ✅
# from abc import ABC, abstractmethod

# class Notificacao(ABC):
#     def __init__(self, mensagem):
#         self.mensagem = mensagem

#     @abstractmethod
#     def enviar(self) -> bool: ...

# class NotificacaoEmail(Notificacao):
#     def enviar(self) -> bool:
#         print('E-mail: enviando - ', self.mensagem)
#         return True

# class NotificacaoSMS(Notificacao):
#     def enviar(self) -> bool:
#         print('SMS: enviando - ', self.mensagem)
#         return False

# def notificar(notificacao: Notificacao):
#     notificacao_enviada = notificacao.enviar()

#     if notificacao_enviada:
#         print('Notificação enviada')
#     else:
#         print('Notificação NÃO enviada')

# notificacao_email = NotificacaoEmail('testando e-mail')
# notificar(notificacao_email)

# notificacao_sms = NotificacaoSMS('testando SMS')
# notificar(notificacao_sms)

# Python Dunder Methods __repr__ e __str__
# Dunder = Double Underscore = __dunder__
# Antigo e útil: https://rszalski.github.io/magicmethods/
# https://docs.python.org/3/reference/datamodel.html#specialnames
# __lt__(self,other) - self < other
# __le__(self,other) - self <= other
# __gt__(self,other) - self > other
# __ge__(self,other) - self >= other
# __eq__(self,other) - self == other
# __ne__(self,other) - self != other
# __add__(self,other) - self + other
# __sub__(self,other) - self - other
# __mul__(self,other) - self * other
# __truediv__(self,other) - self / other
# __neg__(self) - -self
# __str__(self) - str
# __repr__(self) - str
# class Ponto:
#     def __init__(self, x, y, z='String'):
#         self.x = x
#         self.y = y
#         self.z = z

#     def __str__(self):
#         return f'({self.x}, {self.y})'

#     def __repr__(self):
#         # class_name = self.__class__.__name__
#         class_name = type(self).__name__
#         return f'{class_name}(x={self.x!r}, y={self.y!r}, z={self.z!r})'

#     def __add__(self, other):
#         novo_x = self.x + other.x
#         novo_y = self.y + other.y
#         return Ponto(novo_x, novo_y)

#     def __gt__(self, other):
#         resultado_self = self.x + self.y
#         resultado_other = other.x + other.y
#         return resultado_self > resultado_other


# if __name__ == '__main__':
#     p1 = Ponto(4, 2)  # 6
#     p2 = Ponto(6, 4)  # 10
#     p3 = p1 + p2
#     print(p3)
#     print('P1 é maior que p2', p1 > p2)
#     print('P2 é maior que p1', p2 > p1)
#     p4 = Ponto(1, 2)
#     p5 = Ponto(7, 8)
#     print(p4)
#     print(repr(p5))

# __new__ e __init__ em classes Python
# __new__ é o método responsável por criar e
# retornar o novo objeto. Por isso, new recebe cls.
# __new__ ❗️DEVE retornar o novo objeto❗️
# __init__ é o método responsável por inicializar
# a instância. Por isso, init recebe self.
# __init__ ❗️NÃO DEVE retornar nada (None)❗️
# object é a super classe de uma classe
# class A:
#     def __new__(cls, *args, **kwargs):
#         # instancia = object.__new__(A)
#         instancia = super().__new__(cls)
#         return instancia

#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         print('init')

#     def __repr__(self):
#         return 'A()'

# # a = object.__new__(A)
# # a.__init__()
# a = A(123, 456)
# print(a.x, a.y)

# Context Manager com classes - Criando e Usando gerenciadores de contexto
# Você pode implementar seus próprios protocolos # apenas implementando os
# dunder methods que o Python vai usar. Isso é chamado de Duck typing. Um
# conceito relacionado com tipagem dinâmica onde o Python não está interessado
# no tipo, mas se alguns métodos existem no seu objeto para que ele funcione
# de forma adequada.
# Duck Typing:
# Quando vejo um pássaro que caminha como um pato, nada como um pato e grasna
# como um pato, eu chamo aquele pássaro de pato.
# Para criar um context manager, os métodos __enter__ e __exit__
# devem ser implementados.
# O método __exit__ receberá a classe de exceção, a exceção e o traceback.
# Se ele retornar True, exceção no with será suprimidas.
# class MyOpen:
#     def __init__(self, file_path, mode):
#         self.file_path = file_path
#         self.mode = mode
#         self._arquivo = None

#     def __enter__(self):
#         print('OPEN FILE')
#         self._arquivo = open(self.file_path, self.mode)
#         return self._arquivo

#     def __exit__(self, class_exception, exception_, traceback_):
#         print('CLOSE FILE')
#         self._arquivo.close()
#           RECRIANDO A EXCEÇÃO
#         # raise class_exception(*exception_.args).with_traceback(traceback_)
#         # print(class_exception)
#         # print(exception_)
#         # print(traceback_)
#         # exception_.add_note('Qualquer coisa que queira acrescentar')
#           ACRESCENTAR OUTRO ERRO
#         # raise ConnectionError('Não deu para conectar')
#         # return True # ESCONDE OS ERROS

# with MyOpen('aula240.txt', 'w') as file:
#     file.write('Line 1\n')
#     file.writelines('Line 2\nLine 3\n')
#     print('WITH', file)
# from contextlib import contextmanager

# @contextmanager
# def my_open(file_path, mode):
#     try:
#         print('OPEN FILE')
#         file = open(file_path, mode)
#         yield file
#     except Exception as e:
#         print('ERRO:',e)
#     finally:
#         print('CLOSE FILE')
#         file.close()

# with my_open('aula240.txt', 'w') as file:
#     file.write('Line 4\n', 'e')
#     file.writelines('Line 5\nLine 6\n')
#     print('WITH', file)

# Funções decoradoras e decoradores com classes
# def my_repr(self):
#     class_name = self.__class__.__name__
#     class_dict = self.__dict__
#     class_repr = f'{class_name}({class_dict})'
#     return class_repr

# def adiciona_repr(cls):
#     cls.__repr__ = my_repr # PASSA A REFENCIA DA FUNÇÃO
#     return cls # RETORNA A MESMA CLASSE DECORADA

# def my_planet(method):
#     def intern(self, *args, **kwargs):
#         result = method(self, *args, **kwargs)
#         if 'Terra' in result:
#             return "You're in home"
#         return result
#     return intern

# @adiciona_repr # SYNTEX SUGAR
# class Time:
#     def __init__(self, nome):
#         self.nome = nome
# # Time = add_repr(Time) # SOBRESCREVER A CLASSE PARA INSERIR A FUNÇÃO

# @adiciona_repr
# class Planeta:
#     def __init__(self, nome):
#         self.nome = nome

#     @my_planet
#     def return_name(self):
#         return f'Planet: {self.nome}'
# # Planeta = add_repr(Planeta) # SOBRESCREVER A CLASSE PARA INSERIR A FUNÇÃO

# brasil = Time('Brasil')
# marte = Planeta('Marte')
# terra = Planeta('Terra')
# print(brasil)
# print(marte)
# print(terra)
# print(marte.return_name())
# print(terra.return_name())

# REVISÃO CLOSURE
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

# Método especial __call__ -> TRATA DOS PARENTESIS
# callable é algo que pode ser executado com parênteses
# Em classes normais, __call__ faz a instância de uma
# classe "callable".
# class CallMe:
#     def __init__(self, phone):
#         self.phone = phone

#     def __call__(self, nome='Desconhecido'):
#         print(nome, 'está chamando', self.phone)

# call1 = CallMe('35999697879')
# call1('Marcelo')

# Revisão de funções decoradoras
# def make_func(func):
#     def intern(*args, **kwargs):
#         for arg in args:
#             is_digit_(arg)
#             result = func(*args, **kwargs)
#         return result
#     return intern

# @make_func
# def sum_(x, y):
#     return x + y

# def is_digit_(param):
#     if not isinstance(param, (int, float)):
#         raise TypeError('Parameter must to be a number')
#     return param

# numbers = sum_(25, 4)
# print(numbers)

# Classes decoradoras
# class Multiply:
#     def __init__(self, func):
#         self.func = func
#         self._mult = 2
#         # print(func)

#     def __call__(self, *args, **kwargs):
#         # print(args, kwargs)
#         result = self.func(*args, **kwargs)
#         return result * 2

# @Multiply
# def sum_(x, y):
#     return x + y

# numbers = sum_(25,4)
# print(numbers)

# class Multiply:
#     def __init__(self, mult=1):
#         self._mult = mult

#     def __call__(self, func):
#         def intern(*args, **kwargs):
#             print(args, *args, kwargs, *kwargs, func)
#             result = func(*args, **kwargs)
#             return result * self._mult
#         return intern

# @Multiply(2)
# def sum_(x, y):
#     return x + y

# numbers = sum_(25,y=4)
# print(numbers)
