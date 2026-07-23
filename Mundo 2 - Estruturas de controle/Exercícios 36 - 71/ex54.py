from datetime import date

ano_atual = date.today().year

maior_idade = 0
menor_idade = 0

for c in range(0, 7):
    nascimento = int(input('Ano de nascimento: '))
    idade = ano_atual - nascimento
    print(f'{idade} anos.')
    print()

    if idade >= 21:
        maior_idade += 1
    elif idade < 21:
        menor_idade += 1

print()
print(f'{maior_idade} pessoas são maiores de idade')
print(f'{menor_idade} pessoas são menores de idade')
