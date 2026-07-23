def ficha(jogador="<desconhecido>", gols=0):
    print(f"O jogador {jogador} fez {gols} gol(s) no campeonato.")

nome = str(input("Nome do jogador: ")).upper()
gol = str(input("Gols: "))

if gol.isnumeric():
    gol = int(gol)
else:
    gol = 0

if nome.strip() == "":
    ficha(gols=gol)
else:
    ficha(nome, gol)









