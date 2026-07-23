velocidade = float(input('Informe sua velocidade em Km/h: '))
print()
via = 80
limite = via + (via * 5 / 100)


print("Tolerância de 4km/h sobre a velocidade da via"
      "\nVelocidade da via: 80km/h")
print()
print("="*42)


if velocidade > limite:
    multa = (velocidade - limite) * 7
    print(f'Você foi multado por exceder o limite de velocidade de {via} Km/h. Sua multa é de R${multa:.2f}.')


elif velocidade == limite:
    print(f'Você está no limite de velocidade de {via} Km/h. Dirija com segurança!')

else:
    print(f'Você está dentro do limite de velocidade de {via} Km/h. Continue dirigindo com segurança!')