from Validadores import *

def main():
    usuario = Usuario("teste12_")
    email =  Email("teste9@gmail.com")
    senha = Senha("Teste_@10")

    validar_dado(usuario)
    print()
    validar_dado(email)
    print()
    validar_dado(senha)


if __name__ == '__main__':
    main()