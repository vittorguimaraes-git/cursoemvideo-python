texto = "Produtos VG"

print("="*40)
print(texto.center(40))
print("="*40)
print()

produto = float(input('Valor do produto: '))
print()
cartao_debito = produto - (produto * 0.05)
dinheiro = produto - (produto * 0.10)
parcel_2x = produto
parcel_3x = produto + (produto * 0.20)

print('Formas de pagamento:\n')

print(f'[1] - Cartão de débito'
      f'\n 5% de desconto {cartao_debito}')

print()

print(f'[2] - Cartão de crédito 2x'
      f'\n R${produto} ')

print()

print(f'[3] - Cartão de crédito 3x'
      f'\n 20% de juros {parcel_3x}')
print()

print(f'[4] - Á vista'
      f'\n 10% de desconto {dinheiro}')

print()





