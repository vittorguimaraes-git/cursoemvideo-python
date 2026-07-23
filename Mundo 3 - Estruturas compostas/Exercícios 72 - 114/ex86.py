matriz = []
print()
print("[Gerador de Matriz 3x3]".center(30))
print("-"*30)
print()

for l in range(0,3):
    linha = []
    print(f"Linha [{l + 1}]")
    print("-"*30)
    print()

    for c in range(0,3):
        num = int(input(f"Coluna: [{c + 1}]: "))
        linha.append(num)
    matriz.append(linha)
    print()


print()

print("Matrix 3x3".center(32))
print("-"*32)
print()

for linha in matriz:
    for valor in linha:
        print(f"{" ":^2}[{valor:^5}]", end=" ")
    print()
    