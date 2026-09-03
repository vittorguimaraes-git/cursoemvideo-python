from retangulo import Retangulo
from rich import inspect, print

def main():

    r = Retangulo()
    r.base = 12
    r.altura = 15

    inspect(r, private=True, methods=True)


    # r.area = 12
    # r.medidas = -9,-3
    # print(r.medidas)




if __name__ == '__main__':
    main()


