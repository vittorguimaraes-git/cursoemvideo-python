from Funcionario import *

def main():
    gerente = Gerente("Gustavo", 8_000)
    designer = Designer("Isabelly", 5_500)
    desenvolver = Desenvolvedor("Vittor", 6_500)

    print(gerente)
    print()
    print(designer)
    print()
    print(desenvolver)


if __name__ == '__main__':
    main()