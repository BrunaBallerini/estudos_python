

class Cliente:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome.title()

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome
