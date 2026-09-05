import hashlib
from hashlib import sha3_256
from getpass import getpass


class ContaBancaria:

    def __init__(self, id, nome, saldo=0, senha=None):
        self._id = id
        self._titular = nome
        self.__saldo = saldo

        if senha is None:
            senha = self.pedir_senha()

        self.__hash = hashlib.sha3_256(senha.encode('utf-8')).hexdigest()

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

    def pedir_senha(self) -> str:

        while True:
            senha = getpass("Senha: ", echo_char="*")
            if len(senha) < 6:
                print("A senha deve ter pelo menos 6 caracteres.")
            else:
                break

        hash_senha = sha3_256(senha.encode("utf-8")).hexdigest()
        return hash_senha


    def sacar(self, valor: float = 0, chave: str = ""):

        if valor < 0:
            raise ValueError("Valor invalido")

        if valor > self.__saldo:
            raise ValueError("Saldo insuficiente")

        if chave and self.validar_senha(chave):
            self.__saldo -= valor
            return "Saque realizado com sucesso"

        elif not chave:
            senha = self.pedir_senha()
            if senha == self.__hash:
                self.__saldo -= valor
                return "Saque realizado com sucesso"

            else:
                return "Saldo insuficiente"

        else:
            return "Falha na autenticação"




    def validar_senha(self, senha):

        senha_hash = sha3_256(senha.encode()).hexdigest()

        if senha_hash == self.__hash:
            print("Senha validada com sucesso")
            return True
        else:
            print("Senha incorreta")
            return False
