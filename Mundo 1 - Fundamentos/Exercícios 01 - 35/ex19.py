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

escolhido = random.choice(alunos)
print(f"O aluno escolhido foi {escolhido}")
