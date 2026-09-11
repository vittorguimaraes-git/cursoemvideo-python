from abc import ABC, abstractmethod
import re

class Validador(ABC):

    @abstractmethod
    def validar(self, dado):
        pass


class Usuario(Validador):
    def __init__(self, nome):
        valido, status = self.validar(nome)
        self.dado = nome if valido else None
        self.status = status


    def validar(self, nome):
        if not 5 <= len(nome) <= 20:
            return False, "Usuário curto demais, deve ter entre 5 a 20 caracteres!"

        if not any(caractere.isdigit() for caractere in nome):
            return False, "Usuário deve conter ao menos um número!"

        if not nome.islower():
            return False, "Usuário deve estar em minúsculas"

        if " " in nome:
            return False, "Usuário não deve conter espaços"

        return True, "Válido!"

class Senha(Validador):
    def __init__(self, senha):
        valido, status = self.validar(senha)
        self.dado = senha if valido else None
        self.status = status


    def validar(self, senha):

        if not len(senha) >= 8:
            return False, "A senha deve conter ao menos 8 caracteres!"

        if not any(caractere.isupper() for caractere in senha):
            return False, "A senha deve conter ao menos uma letra maiúscula!"

        if not re.search("[^a-zA-Z0-9]", senha):
            return False, "A senha deve conter ao menos um caractere especial!"

        if " " in senha:
            return False, "A senha não deve conter espaços em branco!"

        return True, "Válido!"


class Email(Validador):
    def __init__(self, email):
        valido, status = self.validar(email)
        self.dado = email if valido else None
        self.status = status


    def validar(self, email):

        contador = 0

        for caractere in email:
            if "@" in caractere:
                contador += 1

            if contador > 1:
                return False, "O email não pode conte mais de um @!"

        if "." not in email.split("@")[-1]:
            return False, "O domínio deve conter um ponto antes!"

        if len(email.split(".")[-1]) < 2:
            return False, "A extensão devo conter ao menos duas letras!"

        return True, "Válido!"


def validar_dado(objeto):
    try:
        objeto.validar(objeto.dado)
        print(f"Valor: {objeto.dado}\n"
              f"Status: {objeto.status}")

    except TypeError:
        print(objeto.status)

