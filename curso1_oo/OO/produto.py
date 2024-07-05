class Produto:

    def __init__(self, codigo, preco, quantidade):
        self.__codigo = codigo
        self.__preco = preco
        self.__quantidade = quantidade

    def get_quantidade(self):
        return self.__quantidade

    def set_quantidade(self, nova_quantidade):
        self.__quantidade = nova_quantidade

    def adicionar(self, valor):
        self.__quantidade += valor

    def remover(self, valor):
        self.set_quantidade(self.get_quantidade() - valor)
