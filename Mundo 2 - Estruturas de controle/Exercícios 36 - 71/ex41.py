import datetime

nascimento = int(input("Digite o ano de nascimento:  "))
ano_atual = datetime.date.today().year
idade = ano_atual - nascimento
print()
print(f'Idade: {idade}')

if idade <= 9:
    categoria = 'Mirim'

elif idade <= 14:
    categoria = 'Infantil'

elif idade <= 19:
    categoria = 'Junior'

elif idade <= 20:
    categoria = 'Senior'

else:
    categoria = 'Master'

print(f'Categoria: {categoria}')

