from rich.panel import Panel
from rich import print

class Mensagem:
    def __init__(self, msg, tipo: str = "aviso", icone: str = ":speech_balloon:"):
        self._msg = msg
        self._tipo = tipo.upper()
        self._icone = icone

    def mostrar(self):
        titulo = f"{self._icone} {self._tipo} {self._icone}"
        painel = Panel(self._msg, title=titulo, width=50, style="on black")

        print(painel)


class Alerta(Mensagem):
    def __init__(self, msg):
        super().__init__(msg, "alerta", ":warning:")

    def mostrar(self):
        titulo = f"{self._icone} {self._tipo} {self._icone}"
        painel = Panel(f"[black]{self._msg}[/]", title=titulo, width=50, style= "on yellow", border_style="black")

        print(painel)


class Erro(Mensagem):
    def __init__(self, msg):
        super().__init__(msg, "alerta", ":prohibited:")

    def mostrar(self):
        titulo = f"{self._icone} {self._tipo} {self._icone}"
        painel = Panel(f"[yellow]{self._msg}[/]", title=titulo, width=50, style="on red", border_style="yellow")

        print(painel)