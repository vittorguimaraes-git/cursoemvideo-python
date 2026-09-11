from abc import ABC, abstractmethod

class Funcionario(ABC):

    def __init__(self, nome: str, salario: int|float):

        self.nome = nome.capitalize()
        self.__salario = salario


    @property
    def salario(self):
        return self.__salario

    @salario.setter
    def salario(self, salario):
        if salario > self.__salario:
            self.__salario = salario
        else:
            raise ValueError ("Você não pode reduzir o salário de um funcionário")

    @abstractmethod
    def calcular_bonus(self):
        pass


class Gerente(Funcionario):

    def __init__(self, nome, salario = 0):
        super().__init__(nome, salario)

    def __str__(self):
        return f"{self.nome} ganha {self.salario:,.2f} e como é {self.__class__.__name__} tem um bonus: {self.calcular_bonus():,.2f}"


    def calcular_bonus(self):
        bonus = self.salario * 0.15
        return bonus


class Designer(Funcionario):

    def __init__(self, nome, salario = 0):
        super().__init__(nome, salario)

    def __str__(self):
        return f"{self.nome} ganha {self.salario:,.2f} e como é {self.__class__.__name__} tem um bonus: {self.calcular_bonus():,.2f}"


    def calcular_bonus(self):
        bonus = self.salario * 0.08
        return bonus


class Desenvolvedor(Funcionario):

    def __init__(self, nome, salario = 0):
        super().__init__(nome, salario)

    def __str__(self):
        return f"{self.nome} ganha {self.salario:,.2f} e como é {self.__class__.__name__} tem um bonus: {self.calcular_bonus():,.2f}"


    def calcular_bonus(self):
        bonus = self.salario * 0.1
        return bonus