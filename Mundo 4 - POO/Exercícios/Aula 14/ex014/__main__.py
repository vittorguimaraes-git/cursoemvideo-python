from classes import *

def main():
    x = Analisador()

    x.analisar(100)
    x.analisar("Olá, mundo!")
    x.analisar(3.14)
    x.analisar([1, 2, 3])
    x.analisar({"chave": "valor"})

if __name__ == '__main__':
    main()