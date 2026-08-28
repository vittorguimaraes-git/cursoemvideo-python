from abc import ABC, abstractmethod
from random import randint, choice
from rich import print

class Personagem(ABC):


    def __init__(self, nome, vida):

        self.nome = nome
        self.vida = vida
        self.golpes = ["Soco", "Chute", "Golpe giratório"]


    def atacar(self, alvo, forca) -> None:
        golpe = choice(self.golpes)
        dano = randint(0, forca)


        print(f"[green]{self.nome}[/]({self.vida}) atacou [red]{alvo.nome}[/]({alvo.vida}) com um [blue]{golpe}[/] de força {forca}!")
        print(f"{alvo.nome} recebeu um [red]dano de {dano}[/]!")

    @abstractmethod
    def curar(self):
        pass


class Guerreiro(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)


    def curar(self) -> None:
        cura = randint(1, 100)
        print(f"[blue]{self.nome}[/] enrolou uma atadura nos ferimentos e [green]recuperou {cura} pontos[/] de vida!")


class Mago(Personagem):
    def __init__(self, nome, vida=0):
        super().__init__(nome, vida)


    def curar(self) -> None:
        cura = randint(1, 100)
        print(f"[blue]{self.nome}[/] fez uma mágia de cura e [green]recuperou {cura} pontos[/] de vida!")
