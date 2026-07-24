def contador(i, f, p):
    from time import sleep

    inicio = i
    fim = f
    passo = p

    if p == 0:
        passo = 1

    if p < 0:
        passo *= -1

    if inicio < fim:

        while inicio <= fim:
            print(inicio, end=' ')
            sleep(0.5)
            inicio += passo
        print()

    elif inicio > fim:
        while fim <= inicio:
            print(inicio, end=' ')
            sleep(0.5)
            inicio -= passo





print("-"*50)
print("Contagem de 1 a 10 de um em um")
print("-"*50)
print()

contador(1, 10, 1)
print()


print("-"*50)
print("Contagem de 10 a 0 de dois em dois")
print("-"*50)
print()
contador(10, 0, 2)
print()

print("-"*50)
print("Personalize sua contagem")
print("-"*50)
print()

contador(i=int(input("Inicio: ")), f=int(input("Fim: ")), p=int(input("Passo: ")))
print()





