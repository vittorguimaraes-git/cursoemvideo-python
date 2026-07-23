contador = 0
soma = 0
maior = 0
menor = 0
opcao = 'S'

print('Calculadora de média')
print('-'*30)

while opcao != 'N':

        numero = float(input('Insira um numero: '))
        print()
        opcao = input('Quer continuar? [S/N] ').strip().upper()
        print("-"*30)
        print()

        contador += 1
        soma += numero

        if contador == 1:
            maior = numero
            menor = numero

        else:
            if numero > maior:
                maior = numero

            if numero < menor:
                menor = numero

        while opcao != 'N' and opcao != 'S':
            print('Opção inválida, tente novamente!')
            print()
            opcao = input('Quer continuar? [S/N] ').strip().upper()
            print("-"*30)
            print()



media = soma / contador
print(f'Você digitou {contador} números com um total de {soma} e a média foi {media:.2f}')
print()
print(f'O maior número digitado foi {maior} e o menor foi {menor}')


