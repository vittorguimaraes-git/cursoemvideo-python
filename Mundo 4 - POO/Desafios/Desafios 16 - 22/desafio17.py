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
        painel = Panel(f'{self.nome:^30}\n{"":-^30}\n{f"R$ {self.preco:,.2f}".center(30,'.')}', title='Produto', width=35)

        return painel




produto = Produto('IPHONE 17 PRO MAX', 7800)
print(produto.etiqueta())