def ajuda():
    from time import sleep

    while True:

        print("-"*50)
        print("Sistema de ajuda PyHelp".center(50))
        print("-"*50)
        print()
        sleep(1.3)

        print("[OBS] - Digite 'fim' para sair")
        comando = input("Função ou Biblioteca > ").lower()
        print()

        if comando in "fim":
            print("-" * 35)
            print("Até logo...".center(35))
            print("-"*35)
            sleep(1.3)
            break

        print("-"*50)
        print(f'Acessando o manual do comando "{comando}"')
        print("-"*50)
        print()
        sleep(1.3)

        help(comando)




ajuda()