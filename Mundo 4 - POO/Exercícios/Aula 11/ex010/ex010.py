class Avaliacao:
    def __init__(self, nome, disciplina, nota = 0):

        self.nome = nome
        self.disciplina = disciplina
        self._nota = nota

    #Criando atributo validavel

    @property
    def nota(self): # Getter
        return self._nota

    @nota.setter
    def nota(self, nota): #Setter
        if 0 <= nota <= 10:
            self._nota = nota
        else:
            print("A nota deve ser um valor entre 0 e 10")
