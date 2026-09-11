from Produto import *

def main():
    produto = Produto("Teste", 1000)
    produto2 = Produto("Teste2",2000)
    produto3 = Produto("Teste3", 400)

    carrinho = Carrinho()

    carrinho = carrinho + produto + produto2 + produto3
    print(carrinho)

if __name__ == '__main__':
    main()