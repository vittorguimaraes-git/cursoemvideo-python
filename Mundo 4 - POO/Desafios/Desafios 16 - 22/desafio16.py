# Desafio 16 - Crie uma classe "Funcionario", onde podemos cadastrar nome, setor e cargo.
# Crie também um método que permita ao funcionário se apresentar.


from rich import print

class Funcionario:

    # Atributos

    def __init__(self, nome='<desconhecido>', setor='<desconhecido>', cargo='<desconhecido>'):

        self.empresa = "Curso em vídeo"
        self.nome = nome.capitalize()
        self.setor = setor
        self.cargo = cargo

    # Métodos

    def apresentacao(self):
        return f':handshake: Olá, sou [blue]{self.nome}[/] e sou [blue]{self.cargo}[/] do setor [blue]{self.setor}[/] da empresa {self.empresa}'


funcionario1 = Funcionario('Vittor', 'TI', 'desenvolvedor')
print(funcionario1.apresentacao())

funcionario2 = Funcionario('Gustavo', 'TI', 'diretor')
print(funcionario2.apresentacao())