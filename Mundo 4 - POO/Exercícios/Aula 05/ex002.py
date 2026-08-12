# Declaração de classe

class Gafanhoto:
    """
    -----------------------------------
    Documentação da classe Gafanhoto:
    -----------------------------------

    Essa classe cria um "Gafanhoto(a)"
    com nome e idade

    Para criar um gafanhoto(a), use
    variável = Gafanhoto(nome, idade)

    """

    def __init__(self, nome='<desconhecido>', idade=0): # Método construtor
        # Atributos de instância
        self.nome = nome
        self.idade = idade



    # Parâmetro: nome    # Atributo: self.nome
    # Parâmetro: idade   # Atributo: self.idade
    # OBS: Não são as mesmas Coisas!



    # Métodos de instância
    def aniversario(self):
        self.idade += 1


    # def mensagem(self):
    #     return f'{self.nome} é Gafanhoto(a) e tem {self.idade} anos'

    def __str__(self): # Dunder Method
        return f'{self.nome} é Gafanhoto(a) e tem {self.idade} anos'

    def __getstate__(self):
        return f'Estado: nome = {self.nome}; idade = {self.idade}'



# Declaração de objetos Aula atual
# ____________________________________
g1 = Gafanhoto('Vittor', 21)

# print(g1): Retorna o endereço de memória da classe Gafanhoto()

# Antes:

# <__main__.Gafanhoto object at 0x00000242A48B6CF0>

# Depois:

print(g1)
# ____________________________________


# Atributos Dunders
# ____________________________________

# Docs da classe Gafanhoto():
print(g1.__doc__) # Dunder Attribute

# Formas de exibir o estado de um objeto

# Exibir em forma de dicionário.

print(g1.__dict__) # Atributo

# Com o método __getstate__() é possível
# enviar uma mensagem personalizada.

print(g1.__getstate__()) # Método

print(g1.__class__) # Mostra a classe do objeto
# ____________________________________




# Declaração de objetos Aula anterior
# ____________________________________
#g1 = Gafanhoto()
#g1.nome = 'Gabriel'
#g1.idade = 20

# print(g1.mensagem())  Antes
# g1.aniversario()
# print(g1.mensagem())  Depois
#
# ____________________________________











