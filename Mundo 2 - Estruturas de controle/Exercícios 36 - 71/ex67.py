from time import sleep

i = 1
print('Tabuada'.center(20))
print('='*20)
print()

numero = int(input('Insira um numero: '))
print()
print('='*20)
print()


while True:

    if numero < 0 :
        print('Encerrando programa...')
        sleep(1)
        break

    else:

        produto = numero * i
        print(f'{numero:3}  x{i:3} = {produto}')
        i += 1


        if i > 10:

            print()
            print('='*20)
            print('INFO: Digite um numero negativo para encerrar')
            print('=' * 20)
            print()
            numero = int(input('Insira um numero: '))
            i = 1
            print('='*20 if numero > 0 else '')
