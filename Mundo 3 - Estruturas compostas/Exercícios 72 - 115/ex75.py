tupla = ()
contador = 0

n = True
for n in range(0, 4):
    print()
    numeros = int(input('Digite um numero: '))

    if numeros % 2 == 0:
        contador += 1

    tupla += (numeros,)


for numeros in tupla:
    print()
    print(numeros, end='')

print()
print()

if contador == 1:
    print('Apareceu somente um número par')
elif contador > 1:
    print(f'Apareceram {contador} números pares')

print()

if 9 in tupla:
        print(f'O numero 9 apareceu {tupla.count(9)} vezes')
        print()

if 3 in tupla:
    print(f'O número 3 apareceu na posição {tupla.index(3) + 1}')













