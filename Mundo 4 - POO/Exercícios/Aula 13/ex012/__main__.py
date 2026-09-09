from classes import *

def main():
    pato = Pato("Donald")
    cachorro = Cachorro("Rex")
    gato = Gato("Levi")
    galinha = Galinha("Clóvis")

    pato.emitir_som()
    cachorro.emitir_som()
    gato.emitir_som()
    galinha.emitir_som()

if __name__ == '__main__':
    main()