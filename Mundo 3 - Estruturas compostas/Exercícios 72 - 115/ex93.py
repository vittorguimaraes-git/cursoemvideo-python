saldo = dict()
gols_partida = list()

saldo['Jogador'] = input('Nome do Jogador: ')
saldo['Partidas'] = int(input('Quantidade de Partidas: '))
print()

total = 0
for partida in range(0, saldo['Partidas']):

    gols = int(input(f"{partida + 1}ª Partida"
                          f"\nGols:"))
    gols_partida.append(gols)
    total += gols

    print()


saldo['Gols'] = gols_partida
saldo['Total'] = total
saldo['Media'] = total / saldo['Partidas']

print(f"O jogador {saldo['Jogador']} jogou {saldo['Partidas']} partidas e realizou um total de {saldo['Total']} gols")
print(f"Média por jogo: {saldo['Media']:.2f} gols ")
print()
print(saldo)