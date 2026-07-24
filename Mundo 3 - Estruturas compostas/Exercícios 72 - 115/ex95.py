jogadores = list()
dados = dict()
gols = list()
soma = 0

while True:

    dados['Jogador'] = input('Nome do Jogador: ').capitalize().strip()
    dados['Partidas'] = int(input('Partidas jogadas: '))
    print()

    for partida in range(0, dados['Partidas']):

        gol = int(input(f'Gols na {partida + 1}ª partida : '))
        gols.append(gol)
        soma += gol

    dados['Gols'] = gols.copy()
    dados['Total'] = soma
    print()

    soma = 0
    gols.clear()
    jogadores.append(dados.copy())

    continuar = input('Continuar? [S/N]').upper()[0]
    print()

    if continuar == 'N':
        break


for pos, jogador in enumerate(jogadores, start=1):
    print(f'{pos} - {jogador["Jogador"]} - {jogador["Gols"]} - {jogador["Total"]}'.center(20))

print()

while True:


    escolha = int(input("Escolha um jogador para visualizar as partidas [999 para parar]: "))
    print()

    if escolha == 999:
        break

    jogador = jogadores[escolha - 1]
    print(f"O Jogador [{jogador['Jogador']}] realizou {jogador['Partidas']} partidas.\n")

    for partida, gol in enumerate(jogador['Gols']):
        print(f"Na {partida + 1}ª fez {gol} gols.")
    print()




