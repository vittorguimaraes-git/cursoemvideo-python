from math import sqrt, ceil, pow

cateto_oposto = float(input("Digite o comprimento do cateto oposto: "))
print()

cateto_adjacente = float(input("Digite o comprimento do cateto adjacente: "))
print()

hipotenusa = sqrt(pow(cateto_oposto, 2) + pow(cateto_adjacente, 2))

print(f"O valor da hipotenusa é : {round(hipotenusa, 2)} ou aproximadamente {ceil(hipotenusa)} ")