dados = dict()

"""

dados['Nome'] = input('Nome: ')
dados['Media'] = float(input(f'Media de {dados["Nome"]}: '))

if dados['Media'] >= 7:
    dados['Situacao'] = "Aprovado"

elif dados['Media'] < 7:
    dados['Situacao'] = "Reprovado"

for k, v in dados.items():
    print(f'{k}: {v}') 

"""

nome = input('Nome: ').capitalize().strip()
dados[nome] = float(input(f'Media de {nome}: '))

if dados[nome] >= 7:
    dados['Situacao'] = "Aprovado"

elif dados[nome] < 7:
    dados['Situacao'] = "Reprovado"

for k, v in dados.items():
    print(f'{k}: {v}')

print()
print(dados)