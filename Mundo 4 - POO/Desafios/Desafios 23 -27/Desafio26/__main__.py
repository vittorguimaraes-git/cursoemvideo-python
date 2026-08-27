from funcionarios import *

def main():

    f1 = FuncionarioHorista("Pedro", 12, 200)
    f1.analisar_salario()

    f2 = FuncionarioMensalista("Amanda", 9500)
    f2.analisar_salario()

if __name__ == "__main__":
    main()