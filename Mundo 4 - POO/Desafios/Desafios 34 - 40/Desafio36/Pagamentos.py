from abc import ABC, abstractmethod


class Pagamento(ABC):

    def __init__(self, valor: float|int):

        self._valor = valor

    @property
    def valor_formatado(self):
        return f"R$ {self._valor:,.2f}"


    @abstractmethod
    def pagar(self):
        pass


class Pix(Pagamento):

    def __init__(self, valor: float|int):
        super().__init__(valor)

    def pagar(self):
        print(f"Pagamento CONFIRMADO de {self.valor_formatado} via Pix")


class Boleto(Pagamento):

    def __init__(self, valor: float|int):
        super().__init__(valor)

    def pagar(self):
        print(f"Pagamento CONFIRMADO de {self.valor_formatado} via Boleto")


class CartaoCredito(Pagamento):

    def __init__(self, valor: float|int):
        super().__init__(valor)

    def pagar(self):
        print(f"Pagamento CONFIRMADO de {self.valor_formatado} via Cartão de Credito")


def fazer_pagamento(obj):
    try:
        obj.pagar()
    except AttributeError:
        print(f"O objeto do tipo '{obj.__class__.__name__}' não possui o método 'pagar'")







