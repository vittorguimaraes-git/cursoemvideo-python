def leia_int(msg):

    while True:
        numero = input(msg)

        if numero.isnumeric():
            return int(numero)


        else:
            print('\033[31mERRO! Digite número válido!\033[0m')



def linha(tamanho=42):
    print("-" * tamanho)

def cabecalho(txt):
    linha()
    print(txt.center(42))
    linha()
    print()

def menu(lista):
    cabecalho("Menu do sistema")

    c = 1
    linha(35)
    for opcao in lista:
        print(f"\033[33m{c}\033[34m - \033[m{opcao}\033[m".center(42))
        c += 1
    linha(35)
    escolha = leia_int("\033[32mEscolha uma opção: \033[m ")
    return escolha

def leia_arquivo(nome_arquivo):

    try:
        arquivo = open(nome_arquivo, 'rt')

    except:
        print(f"Erro ao ler o arquivo {nome_arquivo}")

    else:
        cabecalho("Pessoas cadastradas")
        for pessoa in arquivo:
            dados = pessoa.split(';')
            dados[1] = dados[1].replace('\n', '')
            print(f"Nome: {dados[0]}, Idade: {dados[1]}")


def cadastrar_pessoa(arquivo):

    cabecalho("Cadastrando Pessoa")

    try:

        nome = input("Digite seu nome: ")
        idade = int(input("Digite sua idade: "))

    except (TypeError, ValueError):

        print("ERRO: Dados inválidos! Tente novamente.")

    else:
        try:
            arquivo = open(arquivo, 'at')
        except:
            print("ERRO: Ocorreu um erro no arquivo")
        else:
            arquivo.write(f"{nome};{idade}\n")
            arquivo.close()
            print("Pessoa cadastrada com sucesso!")


def sair():
    from time import sleep

    print("Saindo do Sistema.", end="")
    sleep(1)
    print(".", end="")
    sleep(1)
    print(".")
