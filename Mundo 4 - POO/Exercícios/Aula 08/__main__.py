from ex008 import ContaBancaria

def main():
    c1 = ContaBancaria(111, "Maria", 5_000)
    c1.depositar(1000)
    c1._titular = "Pedro" # Ele deixa, mas não mexa, pois 'Adultos estão a consentir'...
    print(c1)


if __name__ == '__main__':
    main()