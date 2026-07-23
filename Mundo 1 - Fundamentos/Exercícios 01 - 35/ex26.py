frase = str(input('Digite uma frase: ')).strip().upper()

a_upper = frase.count('A')
pos_a = frase.find('A') + 1
ultimo_a = frase.rfind('A') + 1

print(f'A frase possui {a_upper} letras "A"')
print(f'A primeira letra "A" está na posição {pos_a}')
print(f'A última letra "A" está na posição {ultimo_a}')
