from termostato import Termostato
from rich import inspect, print

def main():

    t = Termostato()
    t.temperatura = 31
    inspect(t, private=True, methods=True)

if __name__ == '__main__':
    main()


