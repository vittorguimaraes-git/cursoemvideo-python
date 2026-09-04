from abc import ABC, abstractmethod
import datetime

class Pessoa(ABC):
    def __init__(self, nome, nascimento):
        self._nome = nome
        self._nascimento = nascimento

    @property
    def nascimento(self):
        return self._nascimento

    @nascimento.setter
    def nascimento(self, nascimento):
        ano_atual = datetime.date.today().year

        if 1950 < nascimento <= ano_atual:
            self._nascimento = nascimento
        else:
            raise ValueError (f"Ano {ano_atual} é um ano inválido")

    @property
    def idade(self):
        return datetime.datetime.now().year - self._nascimento

    @idade.setter
    def idade(self, idade):
        if idade or not idade:
            raise PermissionError ("Você não pode alterar a idade, mude o ano de nascimento!")


class Aluno(Pessoa):
    def __init__(self, nome, idade, curso):
        super().__init__(nome, idade)

        self.cursos_oficiais = ["ADM", "ADS", "ENG", "CONT"]

        if curso in self.cursos_oficiais:
            self._curso = curso
        else:
            raise ValueError (f"O Curso {curso} não está na lista de cursos oficiais!")



    @property
    def curso(self):
        return self._curso


    @curso.setter
    def curso(self, curso):
        self._curso = curso

    def add_curso(self, curso: str):

        if 3 <= len(curso) <= 5:
            self.cursos_oficiais.append(curso)
        else:
            raise ValueError (f"Somente as 3 ou 5 primeiras letras para adicionar seu curso")





