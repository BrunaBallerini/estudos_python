# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# type: ignore

# import json
# class Funcionario:
#     def __init__(self, nome, sobrenome, nascimento, salario,
#                  funcao, email, endereco):
#         self.nome = nome
#         self.sobrenome = sobrenome
#         self.nascimento = nascimento
#         self.salario = salario
#         self.funcao = funcao
#         self.email = email
#         self.endereco = endereco

#     def nome(self):
#         return self.nome

#     def nome_completo(self):
#         print(f'Funcionário: {self.nome} {self.sobrenome}')

#     def aumento_salario(self, tempo_empresa):
#         if tempo_empresa > 5:
#             self.salario += 500
#             print(f'Func: {self.nome} passou a receber R$ {self.salario}.')

# bruna = Funcionario('Bruna', 'Ballerini', '1989', 3000,
# 'analista de projetos', 'brunaballerini@gmail.com', 'Juscelino Barbosa, 86')
# marcelo = Funcionario('Marcelo', 'Godde', '1989', '10000', 'engenheiro',
# 'marcelohagodde@gmail.com', 'Rua Juscelino Barbosa, 86')
# CAMINHO_ARQUIVO = 'classe_funcionario.json'
# dados = [vars(bruna), vars(marcelo)]

# def fazendo_dump(): # ADIANDO A EXECUÇÃO
#     with open(CAMINHO_ARQUIVO, 'w', encoding='utf8') as arquivo:
#         json.dump(dados, arquivo, ensure_ascii=False, indent=2)

# SOMENTE QUANDO ESSE ARQUIVO FOR EXECUTADO O DUMP SERÁ FEITO
# if __name__ == '__main__':
#     fazendo_dump()

# ESTADOS DENTRO DE UMA CLASSE
# class Camera:
#     def __init__(self, nome, filmando=False):
#         self.nome = nome
#         self.filmando = filmando

#     def filmar(self):
#         if self.filmando:
#             print(f'{self.nome} JÁ está filmando...')
#             return
#         print(f'{self.nome} está filmando...')
#         self.filmando = True

#     def parar_filmar(self):
#         if not self.filmando:
#             print(f'{self.nome} NÃO está filmando...')
#             return
#         print(f'{self.nome} está parando de filmar...')
#         self.filmando = False

#     def fotografar(self):
#         if self.filmando:
#             print(f'{self.nome} não pode fotografar filmando')
#             return
#         print(f'{self.nome} está fotografando...')

# c1 = Camera('Canon')
# c2 = Camera('Sony')
# c1.filmar()
# c1.filmar()
# c1.fotografar()
# c1.parar_filmar()
# c1.fotografar()
# print()
# c2.parar_filmar()
# c2.filmar()
# c2.filmar()
# c2.fotografar()
# c2.parar_filmar()
# c2.fotografar()
# print(c1.__dict__) # ARMAZENA EM UM DICIONÁRIO OS ATRIBUTOS DO OBJETO
# print(vars(c2)) # VARS RETORNA __dict__

# ATRIBUTO DE CLASSE, MÉTODO DE CLASSE, FACTORIES
# class Pessoa:
#     ano = 2023  # ATRIBUTO DE CLASSE
#     def __init__(self, nome, idade):
#         self.nome = nome
#         self.idade = idade

#     @classmethod # MÉTODO DE CLASSE
#     def metodo_de_classe(cls):
#         print('Hey')

# FACTORIES METHOD -> CRIA UM METODO COM ALGO QUE CRIA FORA DA INSTANCIA
#     @classmethod
#     def criar_com_50_anos(cls, nome):
#         return cls(nome, 50)

#     @classmethod
#     def criar_sem_nome(cls, idade):
#         return cls('Anônima', idade)

# p1 = Pessoa('João', 34)
# p2 = Pessoa.criar_com_50_anos('Helena')
# p3 = Pessoa('Anônima', 23)
# p4 = Pessoa.criar_sem_nome(25)
# print(p2.nome, p2.idade)
# print(p3.nome, p3.idade)
# print(p4.nome, p4.idade)

# GETTER, SETTER
# class Conta:
#     def __init__(self, numero, titular, saldo, limite):
#         self.__numero = numero
#         self.__titular = titular
#         self.__saldo = saldo
#         self.__limite = limite

#     def extrato(self):
#         print("Saldo {} da conta do {}".format(self.__saldo, self.__titular))

#     def deposita(self, valor):
#         self.__saldo += valor

#     def __pode_sacar(self, valor_saque):
#         valor_disponivel = self.__saldo + self.__limite
#         return valor_saque <= valor_disponivel

#     def saca(self, valor):
#         if self.__pode_sacar(valor):
#             self.__saldo -= valor
#         else:
#             print("O valor {} ultrapassa o limite.".format(valor))

#     def transfere(self, valor, destino):
#         self.saca(valor)
#         destino.deposita(valor)

#     @property # GETTER
#     def titular(self):
#         return self.__titular

#     @property # GETTER
#     def saldo(self):
#         return self.__saldo

#     @property # GETTER
#     def limite(self):
#         return self.__limite

#     @limite.setter # SETTER
#     def limite(self, limite):
#         self.__limite = limite

#     @staticmethod # STATIC METHOD
#     def codigos_bancos():
#         return {"BB": "001", "Caixa": "104", "Bradesco": "237"}

# conta1 = Conta(123, 'bruna', 5000, 10000)
# conta1.titular = 'mariana'

# class Produto:
#     def __init__(self, codigo, preco, quantidade):
#         self.__codigo = codigo
#         self.__preco = preco
#         self.__quantidade = quantidade

#     @property # GETTER
#     def quantidade(self):
#         return self.__quantidade

#     @quantidade.setter # SETTER
#     def quantidade(self, nova_quantidade):
#         self.__quantidade = nova_quantidade

#     def alterar_quantidade(self, valor):
#         self.__quantidade += valor

#     @property
#     def preco(self):
#         return self.__preco

#     def alterar_preco(self, valor):
#         self.__preco += valor

# caneta = Produto(123, 12.5, 3)
# caneta.alterar_quantidade(5)
# caneta.alterar_preco(3)
# print(caneta.quantidade)
# print(caneta.preco)


# Encapsulamento (modificadores de acesso: public, protected, private)
# Convenções
#   (sem underline) = public
#       pode ser usado em qualquer lugar
# _ (um underline) = protected
#       não DEVE ser usado fora da classe
#       ou suas subclasses.
# __ (dois underlines) = private
#       "name mangling" (desfiguração de nomes) em Python
#       _NomeClasse__nome_attr_ou_method
#       só DEVE ser usado na classe em que foi
#       declarado.

# class Foo:
#     def __init__(self):
#         self.public = 'isso é público'
#         self._protected = 'isso é protegido'
#         self.__private = 'isso é private'

#     def metodo_publico(self):
#         self._metodo_protected()
#         print(self._protected)
#         print(self.__private)
#         self.__metodo_private()
#         return 'metodo_publico'

#     def _metodo_protected(self):
#         print('_metodo_protected')
#         return '_metodo_protected'

#     def __metodo_private(self):
#         print('__metodo_private')
#         return '__metodo_private'

# f = Foo()
# print(f.public)
# print(f.metodo_publico())

# Relações entre classes: associação, agregação e composição
# Associação é um tipo de relação onde os objetos
# estão ligados dentro do sistema.
# Essa é a relação mais comum entre objetos e tem subconjuntos
# como agregação e composição (que veremos depois).
# Geralmente, temos uma associação quando um objeto tem
# um atributo que referencia outro objeto.
# A associação não especifica como um objeto controla
# o ciclo de vida de outro objeto.
class Escritor:
    def __init__(self, nome):
        self.nome = nome
        self._ferramenta = None

    @property
    def ferramenta(self):
        return self._ferramenta

    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self._ferramenta = ferramenta


class FerramentaDeEscrever:
    def __init__(self, nome):
        self.nome = nome

    def escrever(self):
        return f'{self.nome} está escrevendo'


escritor = Escritor('Luiz')
caneta = FerramentaDeEscrever('Caneta Bic')
maquina_de_escrever = FerramentaDeEscrever('Máquina')  # ASSOCIAÇÃO
escritor.ferramenta = maquina_de_escrever
print(caneta.escrever())
print(maquina_de_escrever.escrever())
print(escritor.ferramenta.escrever())

# Agregação é uma forma mais especializada de associação
# entre dois ou mais objetos. Cada objeto terá
# seu ciclo de vida independente.
# Geralmente é uma relação de um para muitos, onde um
# objeto tem um ou muitos objetos.
# Os objetos podem viver separadamente, mas pode
# se tratar de uma relação onde um objeto precisa de
# outro para fazer determinada tarefa.
# (existem controvérsias sobre as definições de agregação).


class Carrinho:
    def __init__(self):
        self._produtos = []

    def total(self):
        return sum([p.preco for p in self._produtos])

    def inserir_produtos(self, *produtos):
        # self._produtos.extend(produtos)
        # self._produtos += produtos
        for produto in produtos:
            self._produtos.append(produto)

    def listar_produtos(self):
        print()
        for produto in self._produtos:
            print(produto.nome, produto.preco)
        print()


class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


carrinho = Carrinho()
p1, p2 = Produto('Caneta', 1.20), Produto('Camiseta', 20)  # DESEMPACOTAMENTO
carrinho.inserir_produtos(p1, p2)  # ASSOCIAÇÃO
carrinho.listar_produtos()
print(carrinho.total())

# Composição é uma especialização da agregação.
# Mas nela, quando o objeto "pai" for apagado, todas
# as referências dos objetos filhos também são
# apagadas.


class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.enderecos = []

    def inserir_endereco(self, rua, numero):
        self.enderecos.append(Endereco(rua, numero))  # COMPOSIÇÃO

    def inserir_endereco_externo(self, endereco):
        self.enderecos.append(endereco)

    def listar_enderecos(self):
        for endereco in self.enderecos:
            print(endereco.rua, endereco.numero)

    def __del__(self):
        print('APAGANDO,', self.nome)


class Endereco:
    def __init__(self, rua, numero):
        self.rua = rua
        self.numero = numero

    def __del__(self):
        print('APAGANDO,', self.rua, self.numero)


cliente1 = Cliente('Maria')
cliente1.inserir_endereco('Av Brasil', 54)
cliente1.inserir_endereco('Rua B', 6745)
endereco_externo = Endereco('Av Saudade', 123213)
cliente1.inserir_endereco_externo(endereco_externo)
cliente1.listar_enderecos()
del cliente1
print(endereco_externo.rua, endereco_externo.numero)
print('AQUI TERMINA MEU CÓDIGO')

# EXERCÍCIO
# class Carro:
#     def __init__(self, nome):
#         self.nome = nome
#         self._motor = None
#         self._fabricante = None

#     @property
#     def motor(self):
#         return self._motor

#     @motor.setter
#     def motor(self, motor):
#         self._motor = motor

#     @property
#     def fabricante(self):
#         return self._fabricante

#     @fabricante.setter
#     def fabricante(self, valor):
#         self._fabricante = valor

# class Motor:
#     def __init__(self, nome):
#         self.nome = nome
# class Fabricante:
#     def __init__(self, nome):
#         self.nome = nome

# camaro = Carro('Camaro')
# v8 = Motor('V8')
# chevrolet = Fabricante('Chevrolet')
# camaro.fabricante = chevrolet
# camaro.motor = v8
# print(camaro.nome, camaro.fabricante.nome, camaro.motor.nome)
# cruze = Carro('Cruze')
# v4 = Motor('V4')
# cruze.fabricante = chevrolet
# cruze.motor = v4
# print(cruze.nome, cruze.fabricante.nome, cruze.motor.nome)
