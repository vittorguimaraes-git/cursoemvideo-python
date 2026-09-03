import hashlib

class Credencial:
    def __init__(self):
        self.__hash = ""

    @property
    def senha(self):
        return self.__hash

    @senha.setter
    def senha(self, chave):
        self.__hash = hashlib.sha3_256(chave.encode()).hexdigest()

    def validar(self, chave):
        senha = hashlib.sha3_256(chave.encode()).hexdigest()

        if senha == self.__hash:
            print("Senha confere!")
            return True

        print("Senha incorreta!")
        return False
