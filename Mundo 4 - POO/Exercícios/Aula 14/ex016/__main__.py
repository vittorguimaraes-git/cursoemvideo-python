from classes import *

def main():
    porta = Porta()
    empresa = Empresa()
    ovo = Ovo()
    pedra = Pedra()

    tentar_abrir(porta)
    tentar_abrir(empresa)
    tentar_abrir(ovo)
    tentar_abrir(pedra)

if __name__ == '__main__':
    main()