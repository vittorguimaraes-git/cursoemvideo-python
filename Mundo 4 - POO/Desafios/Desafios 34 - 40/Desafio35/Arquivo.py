from abc import ABC, abstractmethod


class Arquivo(ABC):

    def __init__(self, nome, tam):
        self.tam = tam / (1000 ** 2)
        self.nome = nome
        self._extensao = None

    @property
    def nome_completo(self):
            return f"{self.nome}.{self._extensao}"

    @abstractmethod
    def abrir(self):
        pass


class PDF(Arquivo):
    def __init__(self, nome, tam):
        super().__init__(nome, tam)

        self._extensao = 'pdf'

    def abrir(self):
        print(f"Abrindo o arquivo '{self.nome_completo}'({self.tam:.2f}MB) no Adobe reader")


class DOC(Arquivo):
    def __init__(self, nome, tam):
        super().__init__(nome, tam)

        self._extensao = 'docx'

    def abrir(self):
        print(f"Abrindo o arquivo '{self.nome_completo}'({self.tam:.2f}MB) no Microsoft Word")


def abrir_arquivo(obj):
    try:
        obj.abrir()
    except AttributeError:
        print(f"O objeto do tipo '{obj.__class__.__name__}' não possui o método 'abrir'")
