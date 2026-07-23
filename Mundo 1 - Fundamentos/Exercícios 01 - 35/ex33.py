numeros = []
maior = None
menor = None

for i in range(0, 3):
    entrada = int(input('Digite um numero: '))
    numeros.append(entrada)

    if maior is None:
        maior = entrada

    if menor is None:
        menor = entrada

    if entrada > maior:
        maior = entrada

    if entrada < menor:
        menor = entrada

print(f'O maior numero digitado foi: {maior}')
print(f'O menor numero digitado foi: {menor}')