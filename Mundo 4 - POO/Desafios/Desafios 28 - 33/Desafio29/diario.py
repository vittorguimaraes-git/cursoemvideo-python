class Diario:

    def __init__(self, senhamestre = 'CeV!@'):

        self.__segredos = []
        self.__senha = senhamestre

    @property
    def senha(self):
        raise PermissionError("Ninguém tem permissão de ver a senha.")


    def escrever(self, msg):
        if isinstance(msg, str) and len(msg) > 0:
            self.__segredos.append(msg.strip())


    def ler(self, senha = "") -> bool:

        if senha == self.__senha:
            print("--- Meu diario ---")
            for segredo in self.__segredos:
                print(segredo)

            return True
        else:
            raise PermissionError("Senha inválida! Você não pode ler meu diário!")


