class Porta:

    def abrir(self):
        print("Girar a maçaneta e empurrar/puxar a porta")

class Empresa:

    def abrir(self):
        print("Vá ao portal do empreendedor com toda a documentação para abrir um CNPJ")

class Ovo:

    def abrir(self):
        print("Quebre a casca e separe as partes em uma frigideira")


class Pedra:
    pass

# Método pythOnico polimorfico Duck Typing

def tentar_abrir(objeto):
    try:
        objeto.abrir()
    except AttributeError:
        print(f"O objeto do tipo '{objeto.__class__.__name__}' não tem o método 'abrir' implementado.")