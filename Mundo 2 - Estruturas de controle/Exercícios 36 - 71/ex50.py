"""Exercício 50 - Faça um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o."""


soma = 0
cont = 0

for c in range(0,6):
    num = int(input('Digite um numero: '))
    print()

    if num % 2 == 0:
        soma += num
        cont += 1
    else:

        print(f'{num} é um número ímpar, ele será desconsiderado!')
        cont += 1
        print()

print(f'Voce informou {cont} números. A soma dos números pares é: {soma}')
