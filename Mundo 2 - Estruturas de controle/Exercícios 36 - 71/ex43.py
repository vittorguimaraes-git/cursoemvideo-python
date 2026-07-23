peso = float(input('Informe seu peso: '))
altura = float(input('Informe sua altura: '))
imc = peso / (altura ** 2)
print(imc)

if imc < 18.5:
    print('Abaixo do peso')

elif 18.5 <= imc < 25:
    print('Peso ideal')

elif 25 <= imc < 30:
    print('Sobre-peso')

elif 30 <= imc < 40:
    print('Obesidade')

elif imc > 40:
    print('Obesidade mórbida')