produto = float(input('Informe o valor: '))
percentual = float(input("% de desconto: "))


desconto = produto - (produto * percentual / 100)


print(desconto)