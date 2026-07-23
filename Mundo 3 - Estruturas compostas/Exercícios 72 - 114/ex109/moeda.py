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

