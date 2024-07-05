# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# type: ignore

# Metaclasses são o tipo das classes
# EM PYTHON, TUDO É UM OBJETO (CLASSES TAMBÉM)
# Então, qual é o tipo de uma classe? (type)
# Seu objeto é uma instância da sua classe
# Sua classe é uma instância de type (type é uma metaclass)
# type('Name', (Bases,), __dict__)
#
# Ao criar uma classe, coisas ocorrem por padrão nessa ordem:
# __new__ da metaclass é chamado e cria a nova classe
# __call__ da metaclass é chamado com os argumentos e chama:
#   __new__ da class com os argumentos (cria a instância)
#   __init__ da class com os argumentos
# __call__ da metaclass termina a execução
#
# Métodos importantes da metaclass
# __new__(mcs, name, bases, dct) (Cria a classe)
# __call__(cls, *args, **kwargs) (Cria e inicializa a instância)
#
# "Metaclasses são magias mais profundas do que 99% dos usuários
# deveriam se preocupar. Se você quer saber se precisa delas,
# não precisa (as pessoas que realmente precisam delas sabem
# com certeza que precisam delas e não precisam de uma explicação
# sobre o porquê)."
# — Tim Peters (CPython Core Developer)

# Foo = type('Foo', (object,), {})
# f = Foo()
# print(type(f))
# print(type(Foo))

# def my_repr(self):
#     return f'{type(self).__name__}({self.__dict__})'

# class Meta(type):
#     def __new__(mcs, name, bases, dct): # CRIA E RETORNA A CLASSE
#         print('META NEW')
#         cls = super().__new__(mcs, name, bases, dct)
#         cls.attr = 1234
#         cls.__repr__ = my_repr
#         if 'speak' not in cls.__dict__ \
#           or not callable(cls.__dict__['speak']):
#             raise NotImplementedError('Implemente falar')
#         return cls
#
#     def __call__(cls, *args, **kwargs): # CRIA E RETORNA A INSTANCIA
#         instancia = super().__call__(*args, **kwargs)
#         if 'nome' not in instancia.__dict__:
#             raise NotImplementedError('Crie o attr nome')
#         return instancia


# class Pessoa(object, metaclass = Meta):
#     def __new__(cls, *args, **kwargs):
#         print('CLASS NEW', args, kwargs)
#         instancia = super().__new__(cls)
#         return instancia

#     def __init__(self, nome):
#         print('CLASS INIT')
#         self.nome = nome

#     def speak(self):
#         print('speaking')

# a = Pessoa('Bruna')
# a.speak()

# Enum -> Enumerações
# Enumerações na programação, são usadas em ocasiões onde temos
# um determinado número de coisas para escolher.
# Enums têm membros e seus valores são constantes.
# Enums em python:
#   - são um conjunto de nomes simbólicos (membros) ligados a valores únicos
#   - podem ser iterados para retornar seus membros canônicos na ordem de
#       definição
# enum.Enum é a superclasse para suas enumerações. Mas também pode ser usada
#   diretamente (mesmo assim, Enums não são classes normais em Python).
# Você poderá usar seu Enum com type annotations, com isinstance e
# outras coisas relacionadas com tipo.
# Para obter os dados:
# membro = Classe(valor), Classe['chave']
# chave = Classe.chave.name
# valor = Classe.chave.value

# import enum
# TIPO   = MÓDULO.CLASSE (NOME)
# Direcoes = enum.Enum('Direcoes',['ESQUERDA', 'DIREITA', 'ACIMA', 'BAIXO'])

# class Direcoes(enum.Enum):
#     ESQUERDA = 1
#     DIREITA = 2
#     ACIMA = 3
#     BAIXO = 4

# def mover(direcao: Direcoes):
#     if not isinstance(direcao, Direcoes):
#         raise ValueError ('Direção não encontrada')
#     print(f'Movendo para {direcao.name}')

# mover(Direcoes.DIREITA)
# mover(Direcoes.ESQUERDA)

# dataclasses - O que são dataclasses?
# O módulo dataclasses fornece um decorador e funções para criar métodos como
# __init__(), __repr__(), __eq__() (entre outros) em classes definidas pelo
# usuário.
# Em resumo: dataclasses são syntax sugar para criar classes normais.
# Foi descrito na PEP 557 e adicionado na versão 3.7 do Python.
# doc: https://docs.python.org/3/library/dataclasses.html
# from dataclasses import asdict, astuple, dataclass


# @dataclass  # @dataclass(init=False, repr=True, frozen=True, order=True)
# class Pessoa:
#     nome: str
#     sobrenome: str
#     idade: int

#     def __post_init__(self):
#         self.nome_completo = f'{self.nome} {self.sobrenome}'

#     @property
#     def nome_completo(self):
#         return f'{self.nome} {self.sobrenome}'

#     @nome_completo.setter
#     def nome_completo(self, valor):
#         nome, *sobrenome = valor.split()
#         self.nome = nome
#         self.sobrenome = ' '.join(sobrenome)


# if __name__ == '__main__':
#     pessoa1 = Pessoa('Bruna', 'Ballerini', 34)
#     print(pessoa1)
#     pessoa1.nome_completo = 'Maria Joana Silva'
#     print(pessoa1.nome_completo)
#     pessoa2 = Pessoa('Marcelo', 'Godde', 34)
#     print(pessoa2.nome_completo)
#     print(asdict(pessoa1).keys())
#     print(asdict(pessoa1).values())
#     print(asdict(pessoa1).items())  # CONVERTE DATACLASS COMO DICIONÁRIO
#     print(astuple(pessoa1)[0])  # CONVERTE DATACLASS COMO TUPLA
#     lista = [Pessoa('A', 'Z', 1), Pessoa('B', 'Y', 2), Pessoa('C', 'X', 3)]
#     ordenadas = sorted(lista, reverse=True, key=lambda p: p.sobrenome)
#     print(ordenadas)


# EXPLICAÇÃO SPLIT
# txt = "welcome to the jungle"
# x = txt.split()
# print(x) #['welcome', 'to', 'the', 'jungle']

# EXPLICAÇÃO JOIN
# myTuple = ("John", "Peter", "Vicky")
# x = "#".join(myTuple)
# print(x) #John#Peter#Vicky

# EXPLICAÇÃO SORTED
# a = ("b", "g", "a", "d", "f", "c", "h", "e")
# x = sorted(a)
# print(x) #['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

# FUNÇÃO PARA SORTED (LAMBDA)
# def ordem_sort_nome(dicionario):
#     return dicionario['nome']


# def ordem_sort_preco(dicionario):
#     return dicionario['preco']

# produtos_preco = sorted(copy.deepcopy(novos_produtos), key=ordem_sort_preco)
# p(produtos_preco)

# Valores padrão e field em dataclasses
# from dataclasses import dataclass, field


# @dataclass
# class Pessoa:
#     nome: str = field(default='Missing')
#     sobrenome: str = field(default='Missing')
#     idade: int = 0
#     enderecos: list[str] = field(default_factory=list)
#     # enderecos: list[str] | None = None

#     def __post_init__(self):
#         self.nome_completo = f'{self.nome} {self.sobrenome}'


# if __name__ == '__main__':
#     pessoa1 = Pessoa('Bruna', 'Ballerini')
#     print(pessoa1)
#     pessoa2 = Pessoa()
#     print(pessoa2)

# namedtuples - tuplas imutáveis com nomes para valores
# Usamos namedtuples para criar classes de objetos que são apenas um
# agrupamento de atributos, como classes normais sem métodos, ou registros de
# bases de dados, etc.
# As namedtuples são imutáveis assim como as tuplas.
# https://docs.python.org/3/library/collections.html#collections.namedtuple
# https://docs.python.org/3/library/typing.html#typing.NamedTuple
# https://brasilescola.uol.com.br/curiosidades/baralho.htm
# from typing import NamedTuple


# class Carta(NamedTuple):
#     valor: str = 'VALOR'
#     naipe: str = 'NAIPE'

# from collections import namedtuple


# Carta = namedtuple('Carta', ['valor', 'naipe'],defaults=['VALOR', 'NAIPE'])
# as_espadas = Carta('A')
# print(as_espadas._asdict())
# print(as_espadas)
# print(as_espadas[0])
# print(as_espadas.valor)
# print(as_espadas[1])
# print(as_espadas.naipe)
# print()
# print(as_espadas._fields)
# print(as_espadas._field_defaults)
# for valor in as_espadas:
#     print(valor)

# Implementando o protocolo do Iterator em Python
# Essa é apenas uma aula para introduzir os protocolos de collections.abc no
# Python. Qualquer outro protocolo poderá ser implementando seguindo a mesma
# estrutura usada nessa aula.
# https://docs.python.org/3/library/collections.abc.html
from collections.abc import Sequence


class MyList(Sequence):
    def __init__(self):
        self._data = {}
        self._index = 0
        self._next_index = 0

    def __getitem__(self, index):
        return self._data[index]

    def __len__(self):
        return self._index

    def append(self, *values):
        for value in values:
            self._data[self._index] = value
            self._index += 1

    def __iter__(self):
        return self

    def __next__(self):
        if self._next_index >= self._index:
            self._next_index = 0
            raise StopIteration
        value = self._data[self._next_index]
        self._next_index += 1
        return value

    def __repr__(self):
        class_name = self.__class__.__name__
        class_list = self._data
        return f'{class_name}, {class_list}'


if __name__ == '__main__':
    list_ = MyList()
    list_.append('Maria', 'Bruna', 'Marcelo')
    print(list_)
    print(len(list_))
    print(list_[1])
    print()
    for item in list_:
        print(item)
    print()
    for item in list_:
        print(item)
