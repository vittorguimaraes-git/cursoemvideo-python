from abc import ABC, abstractmethod

class BebidaQuente(ABC):

    @abstractmethod
    def misturar(self):
        pass


    @abstractmethod
    def servir(self):
        pass


    def preparar(self):
        print(" Iniciando preparo ".center(30, "-"))
        print(f"1. {self.ferver_agua()}")
        print(f"2. {self.misturar()}")
        print(f"3. {self.servir()}")
        print(" Bebida pronta ".center(20, "-"))

    def ferver_agua(self) -> str:
        return "Fervendo água a 100 graus Celsius."


class Cafe(BebidaQuente):

    def misturar(self) -> str:
        return "Passando água pressurizada pelo pó de café moído."


    def servir(self) -> str:
        return  "Servindo em xícara pequena."


class Cha(BebidaQuente):

    def misturar(self) -> str:
        return "Mergulhando sachê de ervas na água."


    def servir(self) -> str:
        return  "Servindo na caneca de porcelana com limão."


class Leite(BebidaQuente):

    def misturar(self) -> str:
        return "Passando vapor pressurizado pelo bico de leite."


    def servir(self) -> str:
        return  "Servindo na caneca grande, já com café."