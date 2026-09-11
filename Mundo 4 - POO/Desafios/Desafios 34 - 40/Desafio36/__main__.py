from Pagamentos import *


def main():

    pix = Pix(3000)
    cartao = CartaoCredito(4000)
    boleto = Boleto(5000)

    fazer_pagamento(pix)
    fazer_pagamento(boleto)
    fazer_pagamento(cartao)



if __name__ == '__main__':
    main()