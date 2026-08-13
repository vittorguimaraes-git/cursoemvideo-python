# Desafio 18 - Crie uma classe chamada "Churrasco", onde seja possível informar
# quantas pessoas vão participar e mostre quanto de carne deve ser comprado, o
# custo total do churrasco e o preço por pessoa.

# CONSIDERE:
# Consumo padrão: 400g por pessoa
# Preço: R$82,40/kg

from rich.panel import Panel
from rich import print


class Churrasco:

    # Atributos

    def __init__(self, titulo, quantidade=0):

        self.pessoas = quantidade
        self.titulo = titulo
        self.consumo = self.pessoas * 0.4
        self.kilos = 82.4
        self.total = self.kilos * self.consumo
        self.valor = self.total / self.pessoas

    # Métodos
    def analisar(self):
        analise = Panel(f'Analisando [green]{self.titulo}[/] com [blue]{self.pessoas}[/]\n'
                        f'Cada participante comerá 400g e cada Kg custa R${self.kilos:,.2f}\n'
                        f'Recomendo [blue]comprar {self.consumo:,.2f}Kg[/]\n'
                        f'O custo total sera de [green]R${self.total:,.2f}[/]\n'
                        f'Cada pessoa pagará [yellow]R${self.valor:,.2f}[/] para participar',title=self.titulo, width=60)

        return analise

c1 = Churrasco('Churra dos amigos', 15)
print(c1.analisar())