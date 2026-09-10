class Numero:

    def __init__(self, valor:int|float = 0):
        self.valor = valor

    def dobrar(self):
        self.valor *= 2

    def __str__(self):
        return f"Tenho o valor {self.valor} dentro do Número"



class Texto:
    def __init__(self, txt:str = ""):
        self.texto = txt

    def __str__(self):
        return f"Tenho o texto '{self.texto}' dentro do Texto"


    def dobrar(self):
        self.texto += " " + self.texto

class Lista:
    def __init__(self, lst:list = []):
        self.valores = lst

    def __str__(self):
        return f"Tenho os itens {self.valores} dentro da Lista"

    def dobrar(self):
        self.valores += self.valores


class Papel:
    def __init__(self):
        self.dobrado = False

    def __str__(self):
        return f"O papel {'está dobrado' if self.dobrado else 'não está dobrado'}"

    def dobrar(self):
        self.dobrado = True

class Casa:
    def __init__(self):
        pass

    def __str__(self):
        return f"Era uma casa, muito engraçada..."

# Duck typing

def tente_dobrar(objeto):
    try:
        objeto.dobrar()

    except AttributeError:
        print(f"O objeto do tipo '{objeto.__class__.__name__}' não pode ser dobrado.")