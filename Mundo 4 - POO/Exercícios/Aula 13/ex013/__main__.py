from classes import *

def main():
    mae = Mae("Jaciara")
    filha = Filha("Isabelly")
    filho = Filho("Matheus")

    mae.fazer_pudim()
    mae.fritar_coxinha()
    filha.fazer_pudim()
    filha.fritar_coxinha()
    filho.fazer_pudim()
    filho.fritar_coxinha()

if __name__ == '__main__':
    main()