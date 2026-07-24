from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep

arq = "cursoemvideo.txt"

if not arquivo_existe(arq):
    criar_arquivo(arq)

while True:
    reposta = menu(["Visualizar cadastros","Cadastrar Pessoas", "Sair do Sistema"])


    if reposta == 1:
        leia_arquivo(arq)
        sleep(1)


    elif reposta == 2:
        cadastrar_pessoa(arq)
        sleep(1)


    elif reposta == 3:
        sair()
        break

