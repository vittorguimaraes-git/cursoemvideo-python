from cafeteria import *

def main():

    leite = Leite()
    cafe = Cafe()
    cha = Cha()

    leite.preparar()
    print()

    cafe.preparar()
    print()

    cha.preparar()


if __name__ == '__main__':
    main()