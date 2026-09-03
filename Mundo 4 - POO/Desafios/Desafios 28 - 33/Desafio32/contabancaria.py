import hashlib
from hashlib import sha3_256
from getpass import getpass


class ContaBancaria:

    def __init__(self, id, nome, saldo=0, senha=None):
        self._id = id
        self._titular = nome
        self.__saldo = saldo

        if senha is None:
            senha = getpass("Senha: ", echo_char="*")

        self.__hash = hashlib.sha3_256(senha.encode()).hexdigest()

    @property
    def nome(self):
        return self._titular

    @nome.setter
    def nome(self, nome):
        if self.pedir_senha():
            self._titular = nome

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor

    def pedir_senha(self) -> bool:

        senha = getpass("Senha: ", echo_char="*")
        verificar_senha = sha3_256(senha.encode()).hexdigest()

        if verificar_senha == self.__hash:
            return True
        else:
            return False

    def sacar(self, valor: float, chave: str = "") -> str:
        print(f"Sacando um valor de R${valor:.2f}")

        if not chave:
            if self.pedir_senha():
                self.__saldo -= valor
                return "Saque realizado com sucesso"
            else:
                return "Senha incorreta"

        else:

            if self.validar_senha(chave):
                self.__saldo -= valor
                return "Saque realizado com sucesso"
            else:
                return "Senha incorreta"

    def validar_senha(self, senha):

        verificar_hash = sha3_256(senha.encode()).hexdigest()

        if verificar_hash == self.__hash:
            print("Senha validada com sucesso")
            return True
        else:
            print("Senha incorreta")
            return False
