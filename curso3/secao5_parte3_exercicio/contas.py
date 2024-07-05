from abc import ABC, abstractmethod


class Conta(ABC):
    def __init__(self, agencia: int, conta: int, saldo: float = 0) -> None:
        self.agencia = agencia
        self.conta = conta
        self._saldo = saldo

    @abstractmethod
    def sacar(self, valor_sacar: float)-> float:
        pass
    def _extrato(self, msg: str = ''):
        print(f'Conta: {self.conta} - Saldo: R${self._saldo:.2f} {msg}')

    def deposito(self, valor_deposito: float):
        self._saldo += valor_deposito
        self._extrato(f'- Deṕosito R${valor_deposito:.2f}')
        return self._saldo

    @abstractmethod
    def __repr__(self) -> str:
        pass
    

class ContaCorrente(Conta):
    def __init__(self, 
                 agencia: int, 
                 conta: int, 
                 saldo: float = 0, 
                 limite: float = 0
                ) -> None:
        super().__init__(agencia, conta, saldo)
        self._limite = limite

    @property
    def limite(self):
        return self._limite
    
    @limite.setter
    def limite(self, limite: float):
        self._limite = limite
        print(f'Limite alterado - R${self._limite:.2f}')
        return self._limite

    def _pode_sacar(self, valor_sacar: float):
        valor_disponivel = self._saldo + self._limite
        return valor_disponivel >= valor_sacar
    
    def sacar(self, valor_sacar: float) -> float:
        if not self._pode_sacar(valor_sacar):
            self._extrato('- Não será possivel retirar o valor.')
            return self._saldo
        self._saldo -= valor_sacar
        self._extrato(f'- Sacado R${valor_sacar:.2f}') 
        return self._saldo
    
    def __repr__(self) -> str:
        class_name = type(self).__name__
        attrs = f'{self.agencia!r}, {self.conta!r}, {self._saldo}, '\
            f' {self._limite!r}'
        return f'({class_name}: {attrs})'
  

class ContaPoupança(Conta):
    def sacar(self, valor_sacar: float) -> float:
        if not valor_sacar <= self._saldo:
            self._extrato('- Não será possivel retirar o valor.')
            return self._saldo
        self._saldo -= valor_sacar
        self._extrato(f'- Sacado R${valor_sacar:.2f}')
        return self._saldo
    
    def __repr__(self) -> str:
        class_name = type(self).__name__
        attrs = f'{self.agencia!r}, {self.conta!r}, {self._saldo!r}'
        return f'({class_name}: {attrs})'


if __name__ == '__main__': # type: ignore
    conta1 = ContaCorrente(7961, 114019)
    conta1.limite = 2000
    conta1.sacar(3000)
    conta1.sacar(2000)
    conta1.sacar(1)
    conta1.deposito(12000)
    print()
    conta2 = ContaPoupança(7961, 254036)
    conta2.sacar(3000.00)
    conta2.deposito(1000)
    conta2.sacar(1000)
    conta2.sacar(1)
