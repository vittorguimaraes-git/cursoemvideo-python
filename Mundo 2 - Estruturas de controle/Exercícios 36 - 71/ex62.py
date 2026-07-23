pa = 0


termos = int(input('Digite quantos termos: '))
print()
primeiro_termo = int(input('Digite o primeiro termo: '))
print()
razao = int(input('Digite a razão: '))
print()

while pa < termos:

    if termos < 1:
        print('ERRO: Digite um termo maior que 0')
        break

    if razao < 1:
        print('ERRO: Digite uma razão maior que 0')
        break

    elif termos:

        resultado = primeiro_termo + (razao * pa)
        pa += 1
        print(resultado)








