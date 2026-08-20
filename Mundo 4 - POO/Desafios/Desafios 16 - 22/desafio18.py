# Desafio 18 - Crie uma classe chamada "Churrasco", onde seja possível informar
# quantas pessoas vão participar e mostre quanto de carne deve ser comprado, o
# custo total do churrasco e o preço por pessoa.

# CONSIDERE:
# Consumo padrão: 400g por pessoa
# Preço: R$82,40/kg

from rich.panel import Panel
from rich import print


class Churrasco:
    #Atributos de classe

    consumo_medio: float = 0.4
    kilos: float = 82.4

    # Atributos

    def __init__(self, titulo, quantidade=0):

        self.pessoas = quantidade
        self.titulo = titulo
        self.consumo = self.pessoas * Churrasco.consumo_medio
        self.total = Churrasco.kilos * self.consumo
        self.valor = self.total / self.pessoas

    # Métodos
    def analisar(self) -> Panel:
        analise = Panel(f'Analisando [green]{self.titulo}[/] com [blue]{self.pessoas} convidados[/]\n'
                        f'Cada participante comerá {Churrasco.consumo_medio:.3f} gramas e cada Kg custa R${Churrasco.kilos:,.2f}\n'
                        f'Recomendo [blue]comprar {self.consumo:,.2f}Kg[/]\n'
                        f'O custo total sera de [green]R${self.total:,.2f}[/]\n'
                        f'Cada pessoa pagará [yellow]R${self.valor:,.2f}[/] para participar',title=self.titulo, width=65)

        return analise

c1 = Churrasco('Churra dos amigos', 15)
print(c1.analisar())