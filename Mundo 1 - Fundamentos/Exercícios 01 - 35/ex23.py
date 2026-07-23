"""num = input('Digite um número de 0 a 9999: ')
for c in range(0, 4):
    print(f'Unidade: {num[c]}')
    print(f'Dezena: {num[c+1]}')
    print(f'Centena: {num[c+2]}')
    print(f'Milhar: {num[c+3]}')"""



num = int(input('Digite um número de 0 a 9999: '))
print(f'Unidade: {num // 1 % 10}')
print(f'Dezena: {num // 10 % 10}')
print(f'Centena: {num // 100 % 10}')
print(f'Milhar: {num // 1000 % 10}')