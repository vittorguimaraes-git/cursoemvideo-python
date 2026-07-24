from time import sleep
def maior(*num):

    total = 0
    maior = 0

    for numeros in num:
        print(f'{numeros} ', end='')
        sleep(0.3)
        total += 1

        if numeros > maior:
            maior = numeros
    print()
    print()

    print(f"foram digitados {total} numeros")
    print(f"O maior número é {maior}")

maior(2, 9, 4, 5, 7, 1)
print()

maior(4, 7, 0)
print()

maior(1, 2)
print()

maior(6)
print()

maior()