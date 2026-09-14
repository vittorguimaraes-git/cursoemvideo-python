from abc import ABC, abstractmethod
import locale


class Pagamento(ABC):

    def __init__(self):

        self._valor = None

    @property
    def valor(self):
        return self._valor

    @valor.setter
    def valor(self, valor):
        if valor > 0:
            self._valor = valor
        else:
            raise ValueError (f"O valor da pagamento deve ser positivo")

    @property
    def valor_formatado(self):
        locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
        return locale.currency(self._valor, grouping=True)


    @abstractmethod
    def pagar(self, valor):
        pass


class Pix(Pagamento):

    def __init__(self):
        super().__init__()

    def pagar(self, valor: float|int):
        self.valor = valor
        print(f"Pagamento CONFIRMADO de {self.valor_formatado} via Pix")


class Boleto(Pagamento):

    def __init__(self):
        super().__init__()

    def pagar(self, valor: float|int):
        self.valor = valor
        print(f"Pagamento CONFIRMADO de {self.valor_formatado} via Boleto")


class CartaoCredito(Pagamento):

    def __init__(self, valor: float|int = 0):
        super().__init__()

    def pagar(self, valor: float|int):
        self.valor = valor
        print(f"Pagamento CONFIRMADO de {self.valor_formatado} via Cartão de Credito")


def fazer_pagamento(obj, valor):
    try:
        obj.pagar(valor)
    except AttributeError:
        print(f"O objeto do tipo '{obj.__class__.__name__}' não possui o método 'pagar'")







