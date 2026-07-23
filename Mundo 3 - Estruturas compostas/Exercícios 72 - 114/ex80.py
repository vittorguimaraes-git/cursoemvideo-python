lista = []

for n in range(0, 5):
    numero = int(input("Digite um numero: "))
    lista.append(numero)


for v in range(0, len(lista)):
    for numero in range(0, len(lista) - v - 1):
        if lista[numero] > lista[numero + 1]:
                # troca os elementos
            lista[numero], lista[numero + 1] = lista[numero + 1], lista[numero]


print("Lista organizada:", lista)
