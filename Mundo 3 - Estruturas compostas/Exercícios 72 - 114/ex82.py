lista = []
pares = []
impares = []

while True:

    numero = int(input('Digite um numero: '))
    lista.append(numero)

    opcao = input('Deseja continuar? [S/N] ').strip().upper()[0]
    print()

    if numero % 2 == 0:
        pares.append(numero)

    elif numero % 2 != 0:
        impares.append(numero)

    if opcao == 'N':
        break


    while opcao != 'S' and opcao != 'N':
        
        print('ERRO| Digite uma opção válida!')
        print()

        opcao = input('Deseja continuar? [S/N] ').strip().upper()[0]
        print()

print(f'A lista digitada foi: {lista}')
print(f'A lista dos pares digitados foi: {pares}')
print(f'A lista dos impares digitados foi: {impares}')