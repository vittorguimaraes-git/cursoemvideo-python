from random import randint
from time import sleep

escolha = int(input('Qual número foi escolhido? '))
bot = randint(1, 5)
print('='*30)
print()
print('Processando...')
sleep(1)
print('Processando...')
sleep(1)
print('Processando...')
sleep(1)
print()

if escolha == bot:
    print('Parabéns, você acertou!')
else:
    print('Que pena, você errou!')
    print(f'O número certo era {bot}.')
