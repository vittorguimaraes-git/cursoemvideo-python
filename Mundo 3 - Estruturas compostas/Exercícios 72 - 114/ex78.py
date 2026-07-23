maior = None
menor = None
lista = []

for n in range(0,5):
    numero = int(input("Digite um numero: "))
    lista.append(numero)

    for numero in lista:

        if maior is None and menor is None:
            maior = numero
            menor = numero

        if numero > maior:
            maior = numero




        if numero < menor:
            menor = numero


print()
print("-"*50)
print(f"O maior numero digitado foi {maior} na posição " , end= "")
for pos, valor in enumerate(lista):
    if valor == maior:
        print(f"{pos}...", end= "")

print()
print(f"O menor numero digitado foi {menor} na posição " , end= "")

for pos, valor in enumerate(lista):
    if valor == menor:
        print(f"{pos}...", end= "")

print()
print("-"*50)







