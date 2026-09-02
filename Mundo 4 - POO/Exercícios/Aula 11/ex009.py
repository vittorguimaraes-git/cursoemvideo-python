class Avaliacao:
    def __init__(self, nome, disciplina, nota):

        self.nome = nome
        self.disciplina = disciplina
        self._nota = nota


    # Métodos Acessores
    def get_nota(self): #Método Getter
        return self._nota


    def set_nota(self, nota):
        if 0 <= nota <= 10:
            self._nota = nota
