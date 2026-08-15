# Desafio 20 - Crie uma classe "Gamer", onde podemos cadastrar nome, nick, e os
# jogos favoritos de uma pessoa. Crie também um método que permita mostrar a ficha desse gamer.

from rich import print
from rich.panel import Panel


class Gamer:

    # Atributos

    def __init__(self, nome, nick='<desconhecido>'):

        jogos = list()

        self.nome = nome
        self.nick = nick
        self.jogos = jogos


    # Métodos

    def add_favoritos(self, jogo):

        self.jogos.append(jogo)

        print(f'[blue]"{jogo}"[/] adicionado com sucesso!')




    def ficha(self):

        jogos_formatados = "\n".join([f":video_game:[blue]{jogo}[/]" for jogo in self.jogos])

        ficha = Panel(

            f'Nome real: {self.nome}\n'
                      f'Jogos favoritos:\n'
                      f'{jogos_formatados}',
                      title=f'Jogador <{self.nick}>',
                      width=40
        )


        print(ficha)



j1 = Gamer('Vittor','NgK')
j1.add_favoritos('DBO')
j1.add_favoritos('Fortinite')
j1.add_favoritos('Roblox')
j1.ficha()
j2 = Gamer('Gabriel','Dipirona')
j2.ficha()