"""Exercício Python 052: Faça um programa que leia um número inteiro e diga se ele é primo ou não é primo."""

divisores = 0
num = int(input('Número: '))


for n in range(1, num + 1):
    if num % n == 0:
        divisores += 1

if divisores == 2:
    print(f'{num} é primo')

elif divisores > 2:
    print(f'{num} não é primo')

elif divisores == 1:
    print('O numero 1 não é primo')

