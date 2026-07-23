lista = []
contador = 0

while True:

    lista.append(int(input('Digite um valor: ')))
    contador += 1
    print()

    opcao = input('Deseja continuar? [S/N] ').strip().upper()[0]
    print()

    if opcao == 'N':
        break

lista.sort(reverse=True)
print(f'Você digitou {contador} números ')
print()
print(f'Lista de forma decrescente: {lista}')
print()


if 5 in lista:
    print(f'O valor 5 apareceu na lista na posição [{lista.index(5)}]')
elif 5 not in lista:
    print('O valor 5 não apareceu na lista')