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

    def __init__(self, raio):
        super().__init__(raio)
        self.raio = raio

    def perimetro(self) -> float :
        return self.raio * 3.14 * 2

    def area(self) -> float :
        return (self.raio ** 2) * 3.14

