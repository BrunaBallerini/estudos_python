"""
Exercício com Abstração, Herança, Encapsulamento e Polimorfismo
Criar um sistema bancário (extremamente simples) que tem clientes, contas e
um banco. A ideia é que o cliente tenha uma conta (poupança ou corrente) e que
possa sacar/depositar nessa conta. Contas corrente tem um limite extra.
Conta (ABC)
    ContaCorrente
    ContaPoupanca
Pessoa
    Cliente
        Clente -> Conta
Banco
    Banco -> Cliente
    Banco -> Conta
Dicas:
Criar classe Cliente que herda da classe Pessoa (Herança)
    Pessoa tem nome e idade (com getters)
    Cliente TEM conta (Agregação da classe ContaCorrente ou ContaPoupanca)
Criar classes ContaPoupanca e ContaCorrente que herdam de Conta
    ContaCorrente deve ter um limite extra
    Contas têm agência, número da conta e saldo
    Contas devem ter método para depósito
    Conta (super classe) deve ter o método sacar abstrato (Abstração e
    polimorfismo - as subclasses que implementam o método sacar)
Criar classe Banco para AGREGAR classes de clientes e de contas (Agregação)
Banco será responsável autenticar o cliente e as contas da seguinte maneira:
    Banco tem contas e clentes (Agregação)
    * Checar se a agência é daquele banco
    * Checar se o cliente é daquele banco
    * Checar se a conta é daquele banco
Só será possível sacar se passar na autenticação do banco (descrita acima)
Banco autentica por um método.
"""

import cliente
import contas

bruna = cliente.Cliente('Bruna', 34)
bruna.conta = contas.ContaCorrente(7961, 114019, 6500, 10000)
bruna.conta.limite = 2000
bruna.conta.sacar(3000)
bruna.conta.sacar(2000)
bruna.conta.sacar(1)
bruna.conta.deposito(12000)
print(bruna)
print(bruna.conta)
print()
marcelo = cliente.Cliente('marcelo', 34)
marcelo.conta = contas.ContaPoupança(7961, 254036, 34000)
marcelo.conta.sacar(3000.00)
marcelo.conta.deposito(1000)
marcelo.conta.sacar(1000)
marcelo.conta.sacar(1)
print(marcelo)
print(marcelo.conta)