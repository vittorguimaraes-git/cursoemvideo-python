maiores = 0
homens = 0
mulheres = 0

while True:

    sexo = input('Digite seu sexo [M/F]: ').strip().upper()[0]
    print('-'*30)
    print()

    while sexo != 'M' and sexo != 'F':
        print('ERRO: Informe um sexo válido!')
        print('-'*30)
        sexo = input('Digite seu sexo [M/F]: ').strip().upper()[0]
        print('-' * 30)
        print()


    idade = int(input('Insira sua idade: '))
    print('-' * 30)
    print()

    while idade < 0:
        print('ERRO: Sua idade não pode ser abaixo de zero!')
        print('-'*30)
        idade = int(input('Insira sua idade: '))
        print('-' * 30)
        print()

    opcao = input('Deseja continuar? [S/N]').strip().upper()[0]
    print('-' * 30)
    print()


    if sexo == 'M' and idade >= 18:
        maiores += 1
        homens += 1

    if sexo == 'F' and 20 > idade >= 18:
            maiores += 1

    if sexo == 'F' and idade < 20:
        mulheres += 1

    if opcao == 'N':

        print(f'Maiores de idade: {maiores}')
        print()
        print(f'Homens cadastrados: {homens}')
        print()
        print(f'Mulheres com menos de 20 anos cadastradas: {mulheres}')
        break


