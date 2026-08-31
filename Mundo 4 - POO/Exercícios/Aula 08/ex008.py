class ContaBancaria:
    """
Simula o funcionamento de uma conta bancária com opção de:
- Saque
- Deposito

    """

    def __init__(self, id, nome, saldo=0 ):
        self.id = id # público (+)
        self._titular = nome # protegido (#)
        self.__saldo = saldo # privado (-)
        print(f'Conta {self.id} criada com sucesso. Saldo atual: {self.__saldo}')

    def __str__(self):
        return f"Estado atual da conta: {self.__dict__}"

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f'R${valor:,.2F} depositado com sucesso!')
        else:
            print('Deposite um valor maior que zero!')

    def sacar(self, valor):
        if 0 <  valor <= self.__saldo:
            self.__saldo -= valor
            print(f'R${valor:,.2F} sacado com sucesso!')
        else:
            print('Saldo insuficiente')


