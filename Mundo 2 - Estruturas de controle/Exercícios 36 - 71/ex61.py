pa = 0
termos = int(input('Quantos termos deseja mostrar? '))
primeiro_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
resultado = primeiro_termo


while pa < termos:

    print(resultado, end=' -> ' if pa < termos - 1 else '')
    resultado += razao
    pa += 1
