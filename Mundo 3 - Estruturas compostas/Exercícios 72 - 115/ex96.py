def area(largura, comprimento):
    area = largura * comprimento

    print(f"A área de um terreno de {largura} x {comprimento} é de {area:.1f}m²")
    return area

print(f"Controle de terreno")
print("-"*30)
print()

largura = float(input("Largura m²: "))
comprimento = float(input("Comprimento m²: "))
area(largura, comprimento)