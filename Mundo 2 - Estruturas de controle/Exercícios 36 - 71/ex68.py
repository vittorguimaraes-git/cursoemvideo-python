from random import randint

print('Jogo do Par ou Impar'.center(40))
print(''.center(40, '='))
print()
v_player = 0


while True:

    computer = randint(0, 10)
    player = input('Escolha Par ou Impar: ').title().strip()
    print('-'*20)
    print()

    while player != 'Par' and player != 'Impar':
        print('ERRO: Escolha inválida!')
        print('-'*25)
        print()
        player = input('Escolha Par ou Impar: ').title().strip()
        print('-'*20)
        print()



    if player == 'Par':

        print(f'Você escolheu [{player}]\n Computador escolheu: [Impar]')
        print('-' *48)
        print()

    elif player == 'Impar':

        print(f'Você escolheu [{player}]'
              f'\nComputador escolheu: [Par]')
        print('-' * 48)
        print()

    numero = int(input('Digite um numero: '))
    print()

    while numero < 0 or numero > 10:
        print('ERRO: Digite um número entre 0 e 10!')
        print('-'*30)
        print()
        numero = int(input('Digite um numero: '))
        print()

    soma = computer + numero

    if soma % 2 == 0 and player == 'Par':
        print(f'Você venceu! O computador escolheu {computer} e você {numero}, e a soma dos números é {soma} que é par')
        print('-'*48)
        print()
        v_player += 1

    elif soma % 2 != 0 and player == 'Par':
        print(f'Você perdeu! O computador escolheu {computer} e você {numero}, e a soma dos números é {soma} que é impar')
        print('-'*48)
        print()
        break

    elif soma % 2 == 1 and player == 'Impar':
        print(f'Você venceu! O computador escolheu {computer} e você {numero}, e a soma dos números é {soma} que é impar')
        print('-'*48)
        print()
        v_player += 1

    elif soma % 2 != 1 and player == 'Impar':
        print(f'Você perdeu! O computador escolheu {computer} e você {numero}, e a soma dos números é {soma} que é par')
        print('-'*48)
        print()
        break


if v_player == 0:
    print('Você não venceu nenhuma vez :(')

else:
    print(f'Você venceu {v_player} vezes :) ')