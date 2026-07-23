valor_casa = float(input('Informe o valor da casa: '))
print(f'R$ {valor_casa:.2f}')

anos = int(input('Quantos anos deseja pagar: '))
salario = float(input('Informe o seu salário: '))
prestacao = valor_casa / (anos * 12)

print(f'R$ {prestacao:.2f}')

if prestacao >= salario * 0.3:
    print('Empréstimo negado! A prestação excede 30% do salário.')
else:
    print('Empréstimo aprovado! A prestação é aceitável.')