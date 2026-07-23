nota_a = float(input('Nota 1: '))
nota_b = float(input('Nota 2: '))
media = (nota_a + nota_b) / 2

if media < 5:
    print('BURRO')

elif 5 <= media < 7 :
    print(f'Média: {media}\n'
          'Você está de recuperação')

else:
    print(f'Média: {media}\n'
          'Passou paizão')
