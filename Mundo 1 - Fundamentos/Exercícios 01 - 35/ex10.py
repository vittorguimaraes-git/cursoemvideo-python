conversor = int(input('Quanto deseja converter? '))
dolar = 3.27

print(f'voce pode converter R${conversor:.2f} para US${round(conversor / dolar, 2)} dólares (cotação: R${dolar})')

