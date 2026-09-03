from diario import Diario
from rich import inspect, print

def main():

    diario = Diario("minhasenha")
    diario.escrever("Entrei no diário")
    diario.ler("minhasenha")


    inspect(diario, private=True, methods=True)

if __name__ == '__main__':
    main()


