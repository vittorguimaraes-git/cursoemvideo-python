# Desafio 22 - Crie uma classe "ControleRemoto", onde vamos simular o funcionamento de um
# controle simples (canal, volume e ligar/desligar)

from rich import print
from rich.panel import Panel

class ControleRemoto:

    CANAL_MIN = 1
    CANAL_MAX = 5
    VOLUME_MIN = 0
    VOLUME_MAX = 4



    def __init__(self, canal= 1, volume= 0):

        # Atributos de instância

        self.ligada : bool = False
        self.canal_atual : int = canal
        self.volume_atual : int = volume


    def tv(self) -> None :

        """
        Mostra o estado atual da televisão caso desligada ou caso ligada
        :return: None
        """

        if not self.ligada:

            tela = ":prohibited: [red]A tv está desligada[/]".center(52)

            tv = Panel(tela, width=40, title="[TV]")
            print(tv)


        else:

            tela = "CANAL  ="

            for canal in range(ControleRemoto.CANAL_MIN, ControleRemoto.CANAL_MAX + 1):
                if canal == self.canal_atual:
                    tela += f" [black on yellow] {canal} [/]"
                else:
                    tela += f" {canal} "

            tela += f"\nVOLUME = "

            for volume in range(ControleRemoto.VOLUME_MIN, ControleRemoto.VOLUME_MAX + 1):
                if volume <= self.volume_atual:
                    tela += f"[black on cyan] [/]"
                else:
                    tela += f"[black on white] [/ ]"

            tv = Panel(tela, width=30, title="[TV]")
            print(tv)






    def ligar_desligar(self) -> bool :

        """
        Alterna o estado do atributo self.ligada para True ou False
        :return: True ou false
        """

        self.ligada = not self.ligada
        return self.ligada





    def comandos(self) -> str :

        """
        Pede a entrada de um comando do usuário
        :return: Uma ‘string’ contendo um comando do usuário
        """

        comando = input(" < CH >  |  - VOL +  |  ON/OF @  |  ")

        match comando:

            case "@":
                self.ligar_desligar()

            case "+":

                if self.ligada:
                    self.volume_atual += 1
                if self.volume_atual > ControleRemoto.VOLUME_MAX:
                    self. volume_atual = ControleRemoto.VOLUME_MAX

            case "-":

                if self.ligada:
                    self.volume_atual -= 1
                if self.volume_atual < ControleRemoto.VOLUME_MIN:
                    self. volume_atual = -1

            case "<":

                if self.ligada:
                    self.canal_atual -= 1
                    if self.canal_atual < ControleRemoto.CANAL_MIN:
                        self.canal_atual = ControleRemoto.CANAL_MAX

            case ">":

                if self.ligada:
                    self.canal_atual += 1
                    if self.canal_atual > ControleRemoto.CANAL_MAX:
                        self.canal_atual = ControleRemoto.CANAL_MIN

            case "0":

                pass

            case _:
                print("[red]Opção inválida.[/]")

        return comando


t1 = ControleRemoto()



while True:

    t1.tv()
    escolha = t1.comandos()
    print()


    if escolha == "0":
        break