def leia_int(msg):

    while True:

        try:
            numero = int(input(msg))

        except (ValueError, TypeError):
            print('\033[31mERRO! Digite número válido!\033[0m')
        else:
            return f"Você acabou de digitar o número {numero}"



print(leia_int("Digite um número inteiro: "))
print()


def leia_float(msg):

    while True:

        try:
            numero = float(input(msg))

        except (ValueError, TypeError):
            print('\033[31mERRO! Digite número válido!\033[0m')
        else:
            return f"Você acabou de digitar o número {numero}"


print(leia_float("Digite um número real: "))
print()