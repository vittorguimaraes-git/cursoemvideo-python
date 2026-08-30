from rich import inspect, print
from poligono import *

def main():
    quadrado = Quadrado(20)
    circulo = Circulo(12)

    # inspect(quadrado, methods=True)

    print(f"Perímetro de um quadrado: {quadrado.perimetro():.1f}cm")
    print(f"Area de um quadrado: {quadrado.area():.1f}cm2")

    print()

    # inspect(circulo, methods=True)
    print(f"Perímetro de um circulo: {circulo.perimetro():.1f}cm")
    print(f"Area de um circulo: {circulo.area():.1f}cm2")


if __name__ == "__main__":
    main()