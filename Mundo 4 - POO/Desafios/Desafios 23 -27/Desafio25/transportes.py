from abc import ABC, abstractmethod

class Transporte(ABC):

    def __init__(self, distancia, frete):

        self.distancia: float = distancia
        self.frete: float = frete

    @abstractmethod
    def calcular_frete(self):
        pass


class Moto(Transporte):

    def __init__(self, distancia, frete=0.50):
        super().__init__(distancia, frete)


    def calcular_frete(self) -> str:
        return f"R${self.distancia * self.frete}"


class Caminhao(Transporte):

    def __init__(self, distancia, frete=1.20):
        super().__init__(distancia, frete)


    def calcular_frete(self) -> str:
        if self.distancia >= 50:
            return f"R${self.distancia * self.frete}"

        else:
            return f"Raio minímo de 50Km"



class Drone(Transporte):

    def __init__(self, distancia, frete=9.50):
        super().__init__(distancia, frete)


    def calcular_frete(self) -> str:
        if self.distancia <= 10:
            return f"R${self.distancia * self.frete}"

        else:
            return f"Raio máximo de 10Km"

