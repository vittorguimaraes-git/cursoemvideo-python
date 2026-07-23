dias = int(input('Tempo de aluguel: '))
km = float(input('Km rodados: '))


valor = (60 * dias) + (0.15 * km)

print(f'O valor a ser pago: {valor:.2f}')