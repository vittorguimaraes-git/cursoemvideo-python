from random import choice
from time import sleep

jogadas = ("Pedra", "Papel", "Tesoura")
texto = "Jokenpô Game"

bot = choice(jogadas).title()


print(texto.center(25))
print("="*25)
print('[] - Pedra'
    '\n[] - Papel'
    '\n[] - Tesoura')
print("="*25)
player = input('  Escolha uma jogada: ').title().strip()
empate = player == bot

print()
print("JÔ", end = " ")
sleep(0.5)
print("KEN", end = " ")
sleep(0.5)
print("PO", end = " ")
sleep(0.5)


print()
print('-'*25)
print(f'Jogador: {player}')
print(f'CPU: {bot}')
print('-'*25)

print()


if player == 'Pedra' and bot == 'Tesoura':
    print(f'{player} ganha de {bot}, parábens você ganhou! :)')


elif player == 'Papel' and bot == 'Pedra':
    print(f'{player} ganha de {bot}, parábens você ganhou!')


elif player == 'Tesoura' and bot == 'Papel':
    print(f'{player} ganha de {bot}, parábens você ganhou!')


elif player == bot:
    print(f'{player} e {bot}, empate! :|')


elif player not in jogadas:
    print('ERRO: Jogada inválida >:(')

else:
    print(f'{bot} ganha de {player}, você perdeu :(')
