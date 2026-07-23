from ex108 import moeda

preco = float(input("Digite um valor: R$ "))
print(f"A metade de {moeda.moeda(preco)} é {moeda.moeda(moeda.metade(preco))}")
print(f"O dobro de {moeda.moeda(preco)} é {moeda.moeda(moeda.dobro(preco))}")
print(f"Aumentando o preço em 10% temos {moeda.moeda(moeda.aumentar(preco, 10))}")
print(f"Diminuindo o preço em 13% temos {moeda.moeda(moeda.diminuir(preco, 13))}")



