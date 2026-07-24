matriz = []
soma = 0
terceira_coluna = 0
maior = 0
print()
print("[Gerador de Matriz 3x3]".center(30))
print("-" * 30)
print()

for l in range(0, 3):
    linha = []
    print(f"Linha [{l + 1}]")
    print("-" * 30)
    print()

    for c in range(0, 3):
        num = int(input(f"Coluna: [{c + 1}]: "))


        if num % 2 == 0:
            soma += num


        linha.append(num)
    matriz.append(linha)
    print()

for linha in matriz:
    terceira_coluna += linha[2]

for valor in matriz[1]:
    if maior < valor:
        maior = valor



    print()

print()

print("Matrix 3x3".center(30))
print("-" * 30)

for linha in matriz:
    for valor in linha:
        print(f"{" ":^2}[{valor:^5}]", end=" ")
    print()
print("-" * 30)
print()



print(f"Maior valor da segunda linha: {maior}")
print(f"Soma da terceira coluna: {terceira_coluna}")
print(f"Soma dos valores pares digitados: {soma}")
