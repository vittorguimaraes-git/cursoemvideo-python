from Exportador import *

def main():
    aluno = Aluno("Maria", "Engenharia", "3")
    usuario = Usuario("maria123", "maria@email.com")

    j = JSON()
    x = XML()

    print(exportar_dados(j, aluno))
    print()

    print(exportar_dados(x, aluno))
    print()

    print(exportar_dados(j, usuario))
    print()

    print(exportar_dados(x, usuario))



if __name__ == '__main__':
    main()