salario = float(input('Informe seu salário: '))


if salario == 1250:
    print('Sem reajuste')

elif salario > 1250:
    salario = salario + (salario * 0.10)
    print('Salário reajustado com aumento de 10%')
    print(f'Salário: {salario} ')


elif salario <= 1250:
    salario = salario + (salario * 0.15)
    print('Salário reajustado com aumento de 15%')
    print(f'Salário: {salario} ')


