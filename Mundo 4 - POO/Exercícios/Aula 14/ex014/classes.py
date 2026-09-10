from functools import singledispatchmethod

class Analisador:

    @singledispatchmethod
    def analisar(self, valor):
        print(f"Tipo não suportado: {type(valor)}")

    @analisar.register
    def _(self, valor: int):
        print(f"{valor} é um número inteiro")

    @analisar.register
    def _(self, valor: str):
        print(f"'{valor}' é uma string")

    @analisar.register
    def _(self, valor: float):
        print(f"{valor} é um número de ponto flutuante")

    @analisar.register
    def _(self, valor: tuple | list | dict):
        print(f"{valor} é uma {type(valor).__name__}")