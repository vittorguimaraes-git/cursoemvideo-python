produtos = (

    ("Tv", 1500),
    ("Sofá", 3000),
    ("Ps5", 3500),
    ("Xbox", 3000)

)

for nome, preco in produtos:
    print(f'{nome:.<30}R${preco:>7}')

