print('-'*30)
print('Somador'.center(30))
print('-'*30)
print()

soma = 0
contador = 0

while True:

    numero = int(input('Digite um número: '))
    print('=' * 30)
    print()
    print('INFO: Digite 999 para parar')
    print()

    if numero == 999:
        print()
        print(f'A soma dos números: {soma}')
        print(f'Quantidade de números digitados: {contador}')
        break
    else:
        soma += numero
        contador += 1



