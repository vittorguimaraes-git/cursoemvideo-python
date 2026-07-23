salario = float(input('Informe seu salário: '))
aumento = float(input('% de aumento desejada: '))

salario_com_aumento = salario + (salario * aumento/100)


print(f'Seu salário com {aumento}% de aumento será R${salario_com_aumento:.2f}')