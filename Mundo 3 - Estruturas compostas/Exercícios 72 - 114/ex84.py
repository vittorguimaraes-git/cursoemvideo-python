pessoas = []
maior = None
menor = None
cont = 0


while True:

    nome = input("Digite seu nome: ")
    peso = float(input("Digite seu peso: "))
    pessoas.append([nome, peso],)
    cont += 1
    opcao = input("Deseja continuar? [S/N] ").upper()[0].strip()

    if maior is None or peso > maior:
        maior = peso
    if menor is None or peso < menor:
        menor = peso


    if opcao == "N":
        break

    elif opcao not in "SN":
        while opcao not in "SN":
            print("Opção inválida!")
            print()
            opcao = input("Deseja continuar? [S/N] ").upper()[0].strip()

print(f"{cont}: Pessoa(s) cadastradas.")
print()
print(f"O maior peso foi de {maior} de ", end="")

for p in pessoas:
    if p[1] == maior:
        print(f"[{p[0]}]")
print()
print(f"O menor peso foi de {menor} de  ", end="")

for p in pessoas:
    if p[1] == menor:
        print(f"[{p[0]}]")
