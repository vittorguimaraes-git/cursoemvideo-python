import random

alunos = [   "Vittor",
             "Isabelly",
             "Larissa",
             "Helena",    ]

print("Alunos:" 
      f"\n {"-"*23}")

for aluno in alunos:
    print(aluno)

print("-"*23)

random.shuffle(alunos) # Embaralha a lista de alunos

print("\n Ordem de sorteio")
for posicao, aluno in enumerate(alunos, start=1):
    print(f"{posicao}º - {aluno}")
print("-"*23)