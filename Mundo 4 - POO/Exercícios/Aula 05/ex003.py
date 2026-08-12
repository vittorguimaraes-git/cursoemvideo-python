class ContaBancaria:
    """
Simula o funcionamento de uma conta bancária com opção de:
- Saque
- Deposito

    """

    def __init__(self, id, nome, saldo=0 ):
        self.id = id
        self.titular = nome
        self.saldo = saldo
        print(f'Conta {self.id} criada com sucesso. Saldo atual: {self.saldo}')

    def __str__(self):
        return (f'Conta: {self.id}\n'
                f'Titular: {self.titular}\n'
                f'Saldo: R$ {self.saldo:,.0f}\n')

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f'R$ {valor:,.0F} depositado com sucesso!')
        else:
            print('Deposite um valor maior que zero!')

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f'R$ {valor:,.0F} sacado com sucesso!')
        else:
            print('Saldo insuficiente')


conta1 = ContaBancaria(112, 'Enzo', 3000)
print(conta1)
conta1.sacar(1000)
print(conta1)
conta1.depositar(2000)
print(conta1)

