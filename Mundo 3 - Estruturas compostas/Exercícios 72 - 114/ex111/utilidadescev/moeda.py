def dobro(valor, formato=False):
    valor = valor * 2
    return valor if formato is False else moeda(valor)


def metade(valor, formato=False):
    valor = valor / 2
    return valor if formato is False else moeda(valor)


def aumentar(valor, porcertagem, formato=False):
    valor = valor + (valor * porcertagem / 100)
    return valor if formato is False else moeda(valor)


def diminuir(valor, porcertagem, formato=False):
    valor = valor - (valor * porcertagem / 100)
    return valor if formato is False else moeda(valor)


def moeda(valor):
    return f'R$ {valor:.2f}'.replace('.', ',')


def resumo(valor, porcentagem, desconto):
    print(f"-"*30)
    print(f"RESUMO DO VALOR".center(30))
    print('-'*30)
    print()

    print(f"-"*35)
    print(f"Valor do produto: \t\t{moeda(valor)}")
    print(f"Metade do valor : \t\t{metade(valor, True)}")
    print(f"O dobro do valor: \t\t{dobro(valor, True)}")
    print(f"Com {porcentagem}% de aumento: \t{aumentar(valor, porcentagem, True)}")
    print(f"Com {desconto}% de desconto: \t{diminuir(valor, porcentagem, True)}")
    print(f"-"*35)

