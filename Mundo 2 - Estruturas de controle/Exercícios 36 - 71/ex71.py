valor = int(input('Insira sua valor para sacar: R$: '))
total = valor
cedulas = 50
total_cedulas = 0


while True:

    if total >= cedulas:
        total -= cedulas
        total_cedulas += 1

    else:
        if total_cedulas > 0:
            print(f'Total de cedulas de R$ {cedulas}: {total_cedulas}')

        if cedulas == 50:
            cedulas = 20
            total_cedulas = 0

        elif cedulas == 20:
            cedulas = 10
            total_cedulas = 0

        elif cedulas == 10:
            cedulas = 1
            total_cedulas = 0

        if total == 0:
            break




