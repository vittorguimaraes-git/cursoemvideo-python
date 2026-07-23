menu = True

print('='*30)
print('Calculadora'.center(30))
print('='*30)
print()



print('[ Insira os valores de A e B ]'.center(30))
print()


a = float(input('A: '))
b = float(input('B: '))
print('-'*30)
print()

print('[1] Somar')
print('[2] Multiplicar')
print('[3] Maior')
print('[4] Novos numeros')
print('[5] Sair')
print('-'*30)

while menu:

    opcao = int(input('Escolha uma opção: '))
    print()

    if opcao == 1:

        print(f'{a} + {b} = {a+b}')
        print()
        print('-' * 30)
        print('[1] Somar')
        print('[2] Multiplicar')
        print('[3] Maior')
        print('[4] Novos numeros')
        print('[5] Sair')
        print('-' * 30)

    elif opcao == 2:

        print(f'{a} x {b} = {a*b}')
        print()
        print('-' * 30)
        print('[1] Somar')
        print('[2] Multiplicar')
        print('[3] Maior')
        print('[4] Novos numeros')
        print('[5] Sair')
        print('-' * 30)


    elif opcao == 3:

        if a > b:
            print(f'{a} > {b}')
            print()
            print('-' * 30)
            print('[1] Somar')
            print('[2] Multiplicar')
            print('[3] Maior')
            print('[4] Novos numeros')
            print('[5] Sair')
            print('-' * 30)

        elif a == b:
            print(f'{a} == {b}')
            print()
            print('-' * 30)
            print('[1] Somar')
            print('[2] Multiplicar')
            print('[3] Maior')
            print('[4] Novos numeros')
            print('[5] Sair')
            print('-' * 30)

        else:
            print(f'{b} > {a}')
            print()
            print('-'*30)
            print('[1] Somar')
            print('[2] Multiplicar')
            print('[3] Maior')
            print('[4] Novos numeros')
            print('[5] Sair')
            print('-' * 30)

    elif opcao == 4:

        a = float(input('A: '))
        b = float(input('B: '))
        print()
        print('-' * 30)
        print('[1] Somar')
        print('[2] Multiplicar')
        print('[3] Maior')
        print('[4] Novos numeros')
        print('[5] Sair')
        print('-' * 30)

    elif opcao == 5:
        print('Saindo do programa...')
        menu = False
