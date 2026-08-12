# Declaração de classe

class Gafanhoto:
    def __init__(self): # Método construtor
        # Atributos de instância
        self.nome = ""
        self.idade = 0

    # Métodos de instância
    def aniversario(self):
        self.idade += 1


    def mensagem(self):
        return f'{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade'

# Declaração de objetos
# __________________________
g1 = Gafanhoto()
g1.nome = 'Vittor'
g1.idade = 21
print(g1.mensagem())
g1.aniversario()
print(g1.mensagem())
# __________________________

print()

# __________________________

g2 = Gafanhoto()
g2.nome = 'Gabriel'
g2.idade = 17
print(g2.mensagem())
g2.aniversario()
print(g2.mensagem())

# __________________________
