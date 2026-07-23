a = int(input("Digite um numero inteiro: "))
b = int(input("Digite outro numero inteiro: "))

maior = a > b

if maior:
    print(f'{a} é o maior.')

elif not maior:
    print(f'{b} é o maior.')

else:
    print('Ambos os números são iguais.')