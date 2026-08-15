# Desafio 21 - Crie uma classe Caneta", que simule o funcionamento de uma caneta
# colorida, podendo escrever frases na cor relativa.

from rich import print


class Caneta:

    # Atributos

    def __init__(self, cor):
        self.cor = cor.capitalize()
        self.tampa = False




    # Métodos

    def destampar(self):
        self.tampa = True

        return self.tampa


    def escrever(self, frase):

        if not self.tampa:
            print(f':x:  A [blue]caneta[/] está tampada!')
        else:

            if self.cor in "Vermelho":
                print(f'[red]{frase}[/]', end="")

            elif self.cor in "Azul":
                print(f'[blue]{frase}[/]', end="")

            elif self.cor in "Verde":
                print(f'[green]{frase}[/]', end="")

            else:
                print('Cor indisponível!')

        return frase


    def quebrar_linha(self, quantidade):

        linhas = "\n" * quantidade

        print(linhas)

    def tampar(self):
        self.tampa = False

        return self.tampa


c1 = Caneta('azul')
c2 = Caneta('vermelho')
c3 = Caneta('verde')

c1.destampar()
c2.destampar()
c3.destampar()


c1.escrever('Olá, tudo bem ?')
c1.quebrar_linha(1)
c2.escrever('Olá, Gafanhoto! ')
c3.escrever('Vamos exercitar!')
