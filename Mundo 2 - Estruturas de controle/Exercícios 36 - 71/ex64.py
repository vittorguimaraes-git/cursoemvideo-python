soma = 0
numero = 0
contador = -1

while numero != 999 :
    numero = int(input('Insira um numero: '))
    print('Digite [999] para parar o programa')
    print("-"*30)

    soma += numero
    contador += 1

print(f'A soma dos números inseridos é: {soma - 999}')
print(f'Você inseriu {contador} números ')

