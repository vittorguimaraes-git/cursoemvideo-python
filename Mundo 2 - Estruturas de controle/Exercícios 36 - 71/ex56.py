"""Exercício Python 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
a media de idade do grupo, o homem mais velho e quantas mulheres tem menos de 20 anos."""


homem_mais_velho = ""
idade_homem = 0
mulher_menos_20 = 0

media_idade = 0
total_idade = 0

for c in range(1, 5):
    print(f'----- {c}ª PESSOA -----')

    nome = input('Nome: ').strip().title()
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').upper().strip()
    total_idade += idade
    print()



    if sexo == 'M' and idade > idade_homem:
        homem_mais_velho = nome
        idade_homem = idade

    if sexo == 'F' and idade < 20:
        mulher_menos_20 += 1



media_idade = total_idade / 4

print()
print(f'O homem mais velho é {homem_mais_velho} com {idade_homem} anos')
print()
print(f'Há {mulher_menos_20} mulheres com menos de 20 anos')
print()
print(f'A média de idade do grupo é {media_idade:.2f} anos')