def arquivo_existe(nome_arquivo):
    try:
        arquivo = open(nome_arquivo, 'rt')
        arquivo.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criar_arquivo(nome_arquivo):
    try:
        arquivo = open(nome_arquivo, 'wt+')
        arquivo.close()

    except:
        print(f"Houve um erro na criação do arquivo {nome_arquivo}")
    else:
        print(f"Arquivo {nome_arquivo} criado com sucesso")


