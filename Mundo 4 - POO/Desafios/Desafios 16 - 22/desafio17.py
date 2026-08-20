# Desafio 17 - Crie a classe "Produto", onde podemos cadastrar nome e o preço.
# Crie também um método que mostre uma etiqueta de preço do produto.




from rich.panel import Panel
from rich import print

class Produto:

    # Atributos

    def __init__(self, nome='<desconhecido>', preco=0):

        self.nome = nome
        self.preco = preco


    # Métodos

    def etiqueta(self):
        nome_formatado = f' {self.nome} '.center(34) + f'{"-"*34}'
        preco_formatado = f' {self.preco:,.0f} '.center(34,".")
        painel = Panel(f"{nome_formatado}\n"
                       f"{preco_formatado}", width=38, title="Produto")

        return painel




produto = Produto('IPHONE 17 PRO MAX', 7800)
print(produto.etiqueta())