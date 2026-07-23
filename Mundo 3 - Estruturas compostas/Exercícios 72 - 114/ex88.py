from random import sample
from time import sleep
palpites = []
jogos = int(input("Quantos jogos deseja jogar: "))

for p in range(jogos):
    jogo = sample(range(0, 60), 6)
    palpites.append(jogo)

for num, cartao in enumerate(palpites):
    print("-"*30)
    print(f"Jogo {num+1}:\n\n {cartao}")
    sleep(1.5)
    print()


"""Código do jogo apenas com for 

from random import randint
palpites = []
jogos = int(input("Quantos jogos deseja jogar: "))
for p in range(jogos):
    palpites.append([])

for jogo in palpites:
    for cartao in range(0, 6):
        jogo.append(randint(0, 60))

for num,cartao in enumerate(palpites):
    print("-"*30)
    print(f"Jogo {num+1}:\n\n {cartao}")
    print() 
                                              """

# Pórem alguns números ainda podem se repetir