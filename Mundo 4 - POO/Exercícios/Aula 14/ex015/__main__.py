from classes import *

def main():
    carteira = Carteira(200)
    carteira2 = Carteira(200)

    carteira += 50
    print(carteira)
    carteira -= 50
    print(carteira)

    if carteira == carteira2:
        print("As carteiras têm o mesmo saldo.")
    else:
        print("As carteiras têm saldos diferentes.")

    if carteira < carteira2:
        print("A segunda carteira tem o saldo maior")

    elif carteira > carteira2:
        print("A primeira carteira tem o saldo maior")

    else:
        print("As carteiras têm o mesmo saldo.")

if __name__ == '__main__':
    main()