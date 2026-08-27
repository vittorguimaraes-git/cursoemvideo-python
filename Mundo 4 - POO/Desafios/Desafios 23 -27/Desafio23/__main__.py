from rich import inspect, print
from poligono import *

def main():
    p1 = Quadrado(20)

    print(f"Perímetro: {p1.perimetro():.1f}")
    print(f"Area: {p1.area():.1f}")


if __name__ == "__main__":
    main()