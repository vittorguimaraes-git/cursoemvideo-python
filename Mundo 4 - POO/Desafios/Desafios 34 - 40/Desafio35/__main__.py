from Arquivo import *
from rich import inspect

def main():
    doc = DOC("prova", 250_000)
    pdf = PDF("contrato", 1_300_000)

    abrir_arquivo(doc)
    abrir_arquivo(pdf)
    inspect(doc)
    inspect(pdf)



if __name__ == '__main__':
    main()