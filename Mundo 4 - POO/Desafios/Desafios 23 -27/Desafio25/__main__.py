from transportes import *

from rich.table import Table
from rich import print

def main():
    dist = 80


    """
    entrega = Drone(dist)
    print(f"Frete de {type(entrega).__name__} em {dist}Km = {entrega.calcular_frete()}")
    """

    viagem = [Moto(dist), Caminhao(dist), Drone(dist)]
    
    tabela = Table(title="Tabela de Fretes" )
    tabela.add_column("Distância")
    tabela.add_column("Tipo")
    tabela.add_column("Frete")

    for entrega in viagem:
        tabela.add_row(f"{dist}km", f"{type(entrega).__name__}", f"{entrega.calcular_frete()}")
    print(tabela)

if __name__ == "__main__":
    main()