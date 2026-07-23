sexo = True

while sexo:

    sexo = input('Sexo: [M/F] ').strip().upper()
    print()



    if sexo == 'M' or sexo == 'F':
        print(f'Sexo registrado com sucesso!')
        sexo = False

    elif sexo != 'M' and sexo != 'F':
        print('ERRO: Informe um sexo válido.')
        print()



