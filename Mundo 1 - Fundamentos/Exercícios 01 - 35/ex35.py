n1 = float(input('Primeiro valor: '))
n2 = float(input('Segundo valor: '))
n3 = float(input('Terceiro valor: '))

if n1 + n2 > n3:
    print('Forma Triângulo')
elif n2 + n3 > n1:
    print('Forma Triângulo')
elif n1 + n3 > n2:
    print('Forma Triângulo')
else:
    print('Não forma triângulo')