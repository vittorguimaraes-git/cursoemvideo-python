import math
from abc import ABC, abstractmethod

class Poligono(ABC):

    def __init__(self, qtd_lados):
        self.qtd_lados = qtd_lados

    @abstractmethod
    def perimetro(self):
        pass

    @abstractmethod
    def area(self):
        pass

class Quadrado(Poligono):

    def __init__(self, lados):
        super().__init__(lados)

        self.lados = lados

    def perimetro(self) -> float :
        return self.lados * 4


    def area(self) -> float :
        return self.lados ** 2


class Circulo(Poligono):

    def __init__(self, raio = 1):
        super().__init__(0)
        self.raio = raio

    def perimetro(self) -> float :
        return self.raio * math.pi * 2

    def area(self) -> float :
        return (self.raio ** 2) * math.pi

