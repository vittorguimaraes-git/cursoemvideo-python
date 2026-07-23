print()
print('Conversor de bases numéricas'
      f'\n{"="*28}')
print()

numero = int(input('Digite um numero inteiro: '))
print()

binario = bin(numero)
octal = oct(numero)
hexadecimal = hex(numero)

while True:

    print('Escolha a base de conversão'
          '\n[1] Binário'
          '\n[2] Octal'
          '\n[3] Hexadecimal')

    print()
    escolha = int(input('Opção: '))
    print("="* 28)
    print()

    if escolha == 1:
        print(f'O número {numero} em binário é: {binario[2:]}')
        break
    elif escolha == 2:
        print(f'O número {numero} em octal é: {octal[2:]}')
        break
    elif escolha == 3:
        print(f'O número {numero} em hexadecimal é: {hexadecimal[2:]}')
        break
    else:
        print('Opção inválida! Tente novamente.')
        print()