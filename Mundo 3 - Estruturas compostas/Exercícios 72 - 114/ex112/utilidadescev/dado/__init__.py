def leiadinheiro(msg):

    while True:

        valor = input(msg)

        if valor.isnumeric():
            return float(valor)
        else:
            print(f'\033[31mErro: "{valor}" não é um valor válido!\033[m')
