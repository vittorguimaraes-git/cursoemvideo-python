# Desafio 22 - Crie uma classe "ControleRemoto", onde vamos simular o funcionamento de um
# controle simples (canal, volume e ligar/desligar)

from rich import print
from rich.panel import Panel

class ControleRemoto:

    def __init__(self):

        self.ligada = False
        self.canal_atual = 1
        self.volume_atual = 0



        if not self.ligada:
            tv = Panel(' [red bold]A TV está desliga [/]'.center(38),
                       title='[ TV ]',
                       width=30

                       )

            print(tv)


            self.comando = input('< CH >  |  - VOL +  |  ON/OFF @ ')
            print("\n")

            if self.comando == '0':
                pass


    def selecionar_canal(self):

        if self.canal_atual == 1:
            return f'[white on yellow] 1 [/]  2   3   4   5'

        elif self.canal_atual == 2:
            return f' 1  [white on yellow] 2 [/]  3   4   5'

        elif self.canal_atual == 3:
            return f' 1   2  [white on yellow] 3 [/]  4   5'

        elif self.canal_atual == 4:
            return f' 1   2   3  [white on yellow] 4 [/]  5'


        elif self.canal_atual == 5:
            return f' 1   2   3   4  [white on yellow] 5 [/]'

        return None


    def selecionar_volume(self):

        if self.volume_atual == 0:
            return f"[cyan on cyan] [/][white on white]    [/]"

        elif self.volume_atual == 1:
            return f"[cyan on cyan]  [/][white on white]   [/]"

        elif self.volume_atual == 2:
            return f"[cyan on cyan]   [/][white on white]  [/]"

        elif self.volume_atual == 3:
            return f"[cyan on cyan]    [/][white on white] [/]"

        elif self.volume_atual == 4:
            return f"[cyan on cyan]     [/][white on white][/]"

        else:
            return f"[red bold] Opção invalida. [/]"






    def ligar(self):

        if self. comando == '@':
            self.ligada = True



    def comandos(self):


        while self.ligada:

            canal_formatado = self.selecionar_canal()
            volume_formatado = self.selecionar_volume()

            tv = Panel(f'CANAL  = {canal_formatado}\n'
                       f'VOLUME = {volume_formatado}', title='[ TV ]', width=40)

            print(tv)


            self.comando = input('< CH >  |  - VOL +  |  ON/OFF @ ')
            print("\n")


            if self.comando == '@':
                self.ligada = False



            elif self.comando == '0':
                break


            elif self.comando == '>':
                self.canal_atual += 1

                if self.canal_atual > 5:
                    self.canal_atual = 1


            elif self.comando == '<':
                self.canal_atual -= 1

                if self.canal_atual < 1:
                    self.canal_atual = 5


            elif self.comando == '+':
                self.volume_atual += 1


            elif self.comando == '-':

                if self.volume_atual >= 0:
                    self.volume_atual -= 1


            else:
                print('[red bold] Opção inválida. [/]')


c1 = ControleRemoto()
c1.ligar()
c1.comandos()