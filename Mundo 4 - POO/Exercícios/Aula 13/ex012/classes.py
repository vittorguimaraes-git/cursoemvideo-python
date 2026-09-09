from abc import ABC

class Animal(ABC):
    def __init__(self, nome:str = ""):
        self.nome = nome

    def emitir_som(self):
        print(f"{self.nome} é um {self.__class__.__name__} e está emitindo um som.")


class Pato(Animal):
    pass

class Cachorro(Animal):
    def emitir_som(self):
        print(f"AU, AU !!!")

class Spitz(Cachorro):
    def emitir_som(self):
        print(f"au! au! au! au! au! au!")

class Pitbull(Cachorro):
    def emitir_som(self):
        print(f"RUF!, RUF!")

class Gato(Animal):
    def emitir_som(self):
        print(f"Miau, Miau !!!")

class Galinha(Animal):
    def emitir_som(self):
        print(f"Pó, pó !!!")
