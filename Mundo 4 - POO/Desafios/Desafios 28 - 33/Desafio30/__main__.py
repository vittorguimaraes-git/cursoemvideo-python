from credencial import Credencial
from rich import inspect, print

def main():

    c = Credencial()
    c.senha = "CeV"

    inspect(c, private=True, methods=True)
    print(c.validar("CeV"))

if __name__ == '__main__':
    main()


