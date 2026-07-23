n = int(input('Digite seu numero: '))

print(f'Tabuada do {n}\n{"-"*20}')
for i in range(0, 11):
    print(f'{n:2} x {i:2} = {n*i:3}')


