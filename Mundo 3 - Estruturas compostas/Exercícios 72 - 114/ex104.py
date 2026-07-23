def leia_int(msg):

    while True:
        numero = input(msg)

        if numero.isnumeric():
            return int(numero)


        else:
            print('\033[31mERRO! Digite número válido!\033[0m')


n = leia_int("Digite um número inteiro: ")
print(f"Você acabou de digitar o número {n}")

