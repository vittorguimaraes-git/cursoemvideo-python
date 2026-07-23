"""Exercício Python 051: Leia o primeiro termo de uma Progressão aritmetica e a sua razão. No final, mostre os 10 primeiros termos dessa progressão."""

primeiro_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))

for a in range(10):
    resultado = primeiro_termo + (razao * a)

    print(resultado)