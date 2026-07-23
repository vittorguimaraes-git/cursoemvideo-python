lista = [[], []]

for num in range(0,7):
    numero = int(input("Digite um numero: "))

    if numero % 2 == 0:
        lista[0].append(numero)

    if numero % 2 != 0:
        lista[1].append(numero)


print(f"Os números pares: {sorted(lista[0])}")
print(f"Os números impares: {sorted(lista[1])}")


