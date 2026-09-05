from contabancaria import ContaBancaria
from rich import inspect, print

def main():
    #print("Criando conta bancaria...")
    #c = ContaBancaria(123, "Vittor", 1000)
    #print(c.sacar(100))

    c = ContaBancaria(123, "Vittor", 10000, senha="123456") # Caso nenhuma senha seja passada como parametro, será pedido a criação dela dentro do main()
    print(c.sacar(100))
    # c.nome = "Roberto"
    inspect(c, private=True, methods=True)

if __name__ == "__main__":
    main()
