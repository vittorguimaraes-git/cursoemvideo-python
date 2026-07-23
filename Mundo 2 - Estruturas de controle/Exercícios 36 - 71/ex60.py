numero = int(input('Digite um número: '))

fatorial = 1
multiplicador = 1

while multiplicador <= numero:
    fatorial *= multiplicador
    multiplicador += 1
    print(fatorial)

"""for numero in range(1, numero + 1):

    fatorial *= multiplicador
    multiplicador += 1
    print(fatorial)"""