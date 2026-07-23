from random import randint

game = True
cpu = randint(0, 10)
contador = 0

while game:
     player = int(input('Tente adivinhar o número que o computador pensou (entre 0 e 10): '))

     if player == cpu:
            print('Parabéns! Você acertou! :)' )
            print()
            game = False

            if contador < 3:
                print(f'Você é um gênio, Acertou em {contador} :)')


     elif player > cpu:
        print('Menos... Tente novamente.')
        print()
        contador += 1
        print(f'Número de tentativas: {contador}')
        print()
     else:
        print('Mais... Tente novamente.')
        print()
        contador += 1
        print(f'Número de tentativas: {contador}')
        print()
