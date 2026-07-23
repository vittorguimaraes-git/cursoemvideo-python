total = 0
produtos_mil = 0
barato = None
caro = None
menor = 0
maior = 0

print("Caixa-pagamento".center(30))
print('-'*30)
print()

while True:

    nome = input('Nome do produto: ')
    valor_produto = float(input('Valor do produto: '))
    print('-'*30)
    total += valor_produto

    opcao = input('Deseja continuar? [Sim/Não] ').upper().strip()[0]
    print('-'*30)
    print()

    while opcao not in 'SN':
        print('ERRO: Digite apenas Sim ou Não!')
        print('-'*30)
        opcao = input('Deseja continuar? [S/N] ').upper().strip()[0]
        print('-' * 30)
        print()

    if valor_produto >= 1000:
        produtos_mil += 1

    if barato is None and caro is None:
        menor = valor_produto
        maior = valor_produto
        barato = nome
        caro = nome

    if valor_produto < menor:
        menor = valor_produto
        barato = nome

    if valor_produto > maior:
        maior = valor_produto
        caro = nome


    if opcao == 'N':
        print(f'Produtos acima de mil reais: {produtos_mil}')
        print(f'O produto mais barato foi: {barato}')
        print(f'O produto mais caro foi: {caro}')
        print(f'O total da compra foi: {total}')
        break






