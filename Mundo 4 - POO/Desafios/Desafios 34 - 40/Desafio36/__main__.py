from Pagamentos import *


def main():

    cartao = CartaoCredito()
    pix = Pix()
    boleto = Boleto()

    print()

    pix.pagar(1354)
    cartao.pagar(1000)
    boleto.pagar(3021)

    print()


    fazer_pagamento(Pix(), 2000)
    fazer_pagamento(CartaoCredito(), 3000)
    fazer_pagamento(Boleto(), 1050)



if __name__ == '__main__':
    main()