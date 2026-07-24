alunos = []
while True:

    nome = str(input("Digite o nome do aluno: ")).capitalize().strip()
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    media = (nota1 + nota2) / 2
    alunos.append([nome, nota1, nota2, media],)
    print()


    opcao = (input("Deseja continuar? [S/N] ")).upper()[0].strip()
    print()

    if opcao == "N":
        break

print("BOLETIM".center(30))
print("-"*30)
print()
print(" Nº - Nome - Media")
print("-"*20)
for pos,dados in enumerate(alunos):
    print(f" {pos} | {dados[0]} | {dados[3]:.2f}")

while True:
    print()
    notas = int(input("Qual aluno deseja ver as notas [999 para sair] ?  "))
    print()

    if notas == 999:
        break


    if 0 <= notas < len(alunos):
        aluno = alunos[notas]
        print(f"As notas de {aluno[0]} são {aluno[1]} e {aluno[2:]}")


    else:
        print("Aluno não encontrado!")





