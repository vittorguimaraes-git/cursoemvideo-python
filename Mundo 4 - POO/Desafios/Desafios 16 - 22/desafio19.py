# Desafio 19 - Crie uma classe "Livro", que simula a passagem de páginas
# de um livro, considerando também se o usuário chegou ao fim da leitura

from rich import print
from rich.panel import Panel
from time import sleep


class Livro:

    # Atributos
    def __init__(self, titulo, total):

        self.paginas = total
        self.titulo =titulo.capitalize()
        self.pagina_atual = 1

        print(f'[blue]:book: Você acabou de abrir o livro [red]"{self.titulo}"[/] que tem [green]{self.paginas} paginas[/]\n'
              f'no total. Você agora esta na [yellow]página {self.pagina_atual}[/]')

    # Método

    def avancar_pagina(self, quantidade):


            for pagina in range(1, quantidade + 1):
                print(f'Pág{self.pagina_atual} ▶︎ ', end="")
                self.pagina_atual += 1
                sleep(0.5)

                if self.pagina_atual == self.paginas:
                    print(f':rotating_light:[red] Você chegou ao final do livro "{self.titulo}"[/].')
                    break


            if self.pagina_atual != self.paginas:
                print(f'[blue]Você avançou {quantidade} paginas e agora esta na [/][yellow]página {self.pagina_atual}[/]')




    # Objetos

livro = Livro('Livro de Desafios', 18)
livro.avancar_pagina(5)
livro.avancar_pagina(10)
livro.avancar_pagina(4)

