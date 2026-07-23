def sorteia():
    from random import randint

    lista = list()
    for c in range(0, 5):
        lista.append(randint(1, 10))
    print(lista)

    return lista


def somar_pares(lista):
    soma = 0

    for c in lista:
        if c % 2 == 0:
            soma += c
    print(soma)





somar_pares(sorteia())
