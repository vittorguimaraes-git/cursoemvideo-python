from random import randint
dicionario = dict()

maior = 0
cont = 0

for jogador in range(0, 4):
    jogada = randint(1, 6)

    if jogada > maior:
        maior = jogada

    print(f'Jogador {jogador + 1}: {jogada} ')
    print()
    dicionario[jogador + 1] = jogada

lista = list(dicionario.items())
lenght = len(lista)

for i in range(lenght):
    for j in range(0,lenght - i - 1):
        if lista[j][1] > lista[j + 1][1]:
            lista[j], lista[j + 1] = lista[j + 1], lista[j]


dicionario_ordenado = dict(lista)

print("Ranking final:".center(50, "-"))
print()
for posicao, (jogador, jogada) in enumerate(dicionario_ordenado.items(), start=1):
    print(f'{posicao}º lugar - Jogador {jogador}: {jogada}'.center(50))
print()
print("-"*50)
print()
