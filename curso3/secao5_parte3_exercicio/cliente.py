from contas import Conta, ContaCorrente, ContaPoupança


class Pessoa:
    def __init__(self, nome: str, idade: int) -> None:
        self._nome = nome
        self._idade = idade

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, novo_nome: str):
        self._nome = novo_nome
    
    @property
    def idade(self):
        return self._idade
    
    @idade.setter
    def idade(self, nova_idade: int):
        self._idade = nova_idade

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'{self._nome!r}, {self._idade!r}'
        return f'({class_name}: {attrs})'

  
class Cliente(Pessoa):
    def __init__(self, nome: str, idade: int) -> None:
        super().__init__(nome, idade)
        self.conta: Conta | None = None

    # def tem_conta(self):
    #     if self.conta:
    #         print('Cliente não tem conta.')
    #     self.conta = True


if __name__ == '__main__': # type: ignore
    bruna = Cliente('Bruna', 34)
    bruna.conta = ContaCorrente(7961, 114019, 6500, 10000)
    print(bruna)
    print(bruna.conta)
    print()
    marcelo = Cliente('marcelo', 34)
    marcelo.conta = ContaPoupança(7961, 254036, 34000)
    print(marcelo)
    print(marcelo.conta)
    


# OUTRA FORMA DE ADICIONAR O REPR
# def my_repr(self):
#     class_name = self.__class__.__name__
#     class_dict = self.__dict__
#     class_repr = f'{class_name}({class_dict})'
#     return class_repr

# def adiciona_repr(cls):
#     cls.__repr__ = my_repr # PASSA A REFENCIA DA FUNÇÃO
#     return cls # RETORNA A MESMA CLASSE DECORADA

# @adiciona_repr # SYNTEX SUGAR
# class ___