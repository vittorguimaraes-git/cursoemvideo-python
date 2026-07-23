elementos = int(input('Digite quantos elementos: '))

termo1 = 0
termo2 = 1
contador = 0

while contador < elementos:

    print(termo1, end=' -> ' if contador < elementos - 1 else '')
    termo3 = termo1 + termo2
    termo1 = termo2
    termo2 = termo3
    contador += 1