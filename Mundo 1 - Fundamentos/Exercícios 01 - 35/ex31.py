viagem = float(input('Informe a distância da viagem em Km: '))
if viagem <= 200:
    custo = viagem * 0.50
else:
    custo = viagem * 0.45
print(f'O custo da viagem é de R${custo:.2f}.')