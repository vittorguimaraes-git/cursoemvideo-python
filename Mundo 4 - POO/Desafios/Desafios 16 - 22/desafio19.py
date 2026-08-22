# Desafio 19 - Crie uma classe "Livro", que simula a passagem de páginas
# de um livro, considerando também se o usuário chegou ao fim da leitura

from rich import print
from time import sleep


class Livro:


    def __init__(self, titulo, total):

        # Atributos de instância

        self.paginas = total
        self.titulo = titulo.capitalize()
        self.pagina_atual = 1

        print(f'[blue]:book: Você acabou de abrir o livro [red]"{self.titulo}"[/] que tem [green]{self.paginas} paginas[/]\n'
              f'no total. Você agora esta na [yellow]página {self.pagina_atual}[/]')


        # Método


    def fim_livro(self) -> bool:

        return True if self.pagina_atual == self.paginas else False


    def avancar_pagina(self, quantidade=1) -> None:

            if not self.fim_livro():

                contador = 0
                for pagina in range(0, quantidade, 1):

                    if not self.fim_livro():
                        print(f'Pág{self.pagina_atual} ▶︎ ', end="")
                        self.pagina_atual += 1
                        sleep(0.4)
                        contador += 1
                print(f'[blue]Você avançou {contador} paginas e agora esta na [/][yellow]página {self.pagina_atual}[/]')

                if self.fim_livro():
                    print(f':closed_book:[red] Você chegou ao final do livro "{self.titulo}"[/].')

            else:
                print(f'[red] Sem mais páginas para ler[/].')


        # Objetos

livro = Livro('Livro de Desafios', 18)
livro.avancar_pagina(5)
livro.avancar_pagina(10)
livro.avancar_pagina(4)
livro.avancar_pagina(1)


