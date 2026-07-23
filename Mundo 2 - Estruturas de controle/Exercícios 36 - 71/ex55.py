maior_peso = 0
menor_peso = 0

for p in range(1, 6):
    peso = float(input('Peso: '))

    if p == 1:
        maior_peso = peso
        menor_peso = peso

    else:

        if peso > maior_peso:

            maior_peso = peso

        if peso < menor_peso:

            menor_peso = peso

print()
print(f'O maior peso é {maior_peso:.2f} kg')
print(f'O menor peso é {menor_peso:.2f} kg')