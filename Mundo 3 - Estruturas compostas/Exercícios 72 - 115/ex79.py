lista = []

print('Gerador de Lista ordenadas'.center(42))
print('-'*42)
print()

while True:

    numero = int(input('Insira um numero: '))
    print()

    if numero not in lista:
        lista.append(numero)

    elif numero in lista:
        print('-' * 42)
        print(f'ERRO: Número já registrado na posição [{lista.index(numero)}]')
        print('-' * 42)
        print()


    opcao = input('INFO: Deseja continuar? [S/N] ').strip().upper()[0]
    print()
    print('-' * 42)

    if opcao == 'S':
            continue

    elif opcao == 'N':

        print(f'Lista original: {lista}')
        print()
        print(f'Lista ordenada: {sorted(lista)}')
        break

    else:
        print('ERRO: Responda apenas S ou N!')



