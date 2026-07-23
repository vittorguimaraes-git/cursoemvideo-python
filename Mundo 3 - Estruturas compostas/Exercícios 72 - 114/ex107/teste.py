from ex107 import moeda

preco = float(input("Digite um valor: R$"))
print(f"A metade de {preco} é {moeda.metade(preco)}")
print(f"O dobro de {preco} é {moeda.dobro(preco)}")
print(f"Aumentando o preço em 10% temos {moeda.aumentar(preco, 10)}")
print(f"Diminuindo o preço em 13% temos {moeda.diminuir(preco, 13)}")



