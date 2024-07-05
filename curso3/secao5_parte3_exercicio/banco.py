import cliente
import contas


class Banco:
    def __init__(self, 
                 codigo_banco: int,
                 agencias: list[int] | None = None,
                 clientes: list[cliente.Cliente] | None = None,
                 contas: list[contas.Conta] | None = None,
                ) -> None:
        self.codigo_banco = codigo_banco
        self.agencias = agencias or []
        self.clientes = clientes or []
        self.contas = contas or []
    
    def _checa_agencia(self, conta):
        if conta.agencia in self.agencias:
            print('checa_agencia', True)
            return True
        print('checa_agencia', False)
        return False

    def _checa_cliente(self, cliente):
        if cliente in self.clientes:
            print('checa_cliente', True)
            return True
        print('checa_cliente', False)
        return False

    def _checa_conta(self, conta):
        if conta in self.contas:
            print('checa_conta', True)
            return True
        print('checa_conta', False)
        return False

    def _checa_conta_cliente(self, cliente: cliente.Cliente, conta: contas.Conta):
        if conta is cliente.conta:
            print('checa_conta_cliente', True)
            return True
        print('checa_conta_cliente', False)
        return False
    
    def autenticar(self, cliente: cliente.Cliente, conta: contas.Conta):
        return self._checa_agencia(conta) \
            and self._checa_cliente(cliente) \
            and self._checa_conta(conta) \
            and self._checa_conta_cliente(cliente, conta)

    def __repr__(self) -> str:
        class_name = type(self).__name__
        attrs = f'{self.agencias!r}, {self.clientes!r}, {self.contas!r}'
        return f'({class_name}: {attrs})'


if __name__ == '__main__': 
    bruna = cliente.Cliente('bruna', 34)
    conta1 = contas.ContaCorrente(7961, 114019, 6500, 10000)
    bruna.conta = conta1

    marcelo = cliente.Cliente('marcelo', 34)
    conta2 = contas.ContaPoupança(7961, 254036, 34000)
    marcelo.conta = conta2

    banco = Banco(565)
    banco.clientes.extend([bruna, marcelo])
    banco.contas.extend([conta1, conta2])
    banco.agencias.extend([7961, 7962, 7963])
    print(banco)
    # print(banco.autenticar(bruna, conta1))
    # print(banco.autenticar(marcelo, conta1))

    if banco.autenticar:
        conta1.deposito(500)
        marcelo.conta.sacar(1000)

# EXPLICAÇÃO EXTEND  
# fruits = ['apple', 'banana', 'cherry']
# cars = ['Ford', 'BMW', 'Volvo']
# other = []
# other.extend([fruits, cars])
# print(other)