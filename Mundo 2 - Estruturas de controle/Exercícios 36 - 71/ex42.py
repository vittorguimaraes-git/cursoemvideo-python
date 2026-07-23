n1 = float(input('Primeiro valor: '))
n2 = float(input('Segundo valor: '))
n3 = float(input('Terceiro valor: '))


if n1 + n2 > n3 and n1 + n3 > n2 and n2 + n3 > n1:
    print('Forma Triângulo')

    if n1 == n2 == n3:
        print('Triângulo Equilátero')
    elif n1 != n2 and n2 != n3 and n3 != n1:
        print('Triângulo Escaleno')
    else:
        print('Triângulo Isósceles')
else:
    print('Não forma triângulo')
