class Retangulo:

    def __init__(self, base = 1, altura = 1):
        self._base = base
        self._altura = altura
        self._area = None


    @property
    def base(self):
        return self._base

    @property
    def altura(self):
        return self._altura

    @property
    def area(self):
        return self._base * self._altura


    @property
    def medidas(self):
        return (f"Base = {self._base}\n"
                f"Altura = {self._altura}\n"
                f"Area = {self.area}")


    @base.setter
    def base(self, base):
        if base > 0:
            self._base = base
        else:
            raise ValueError ("Valor inválido para base")



    @altura.setter
    def altura(self, altura):
        if self._altura > 0:
            self._altura = altura
        else:
            raise ValueError ("Valor inválido para altura")

    @area.setter
    def area(self):
        area = self.base * self.altura


    @medidas.setter
    def medidas(self, medidas):
        if medidas[0] > 0:
            self._base = medidas[0]
        if medidas[1] > 0:
            self._altura = medidas[1]
        else:
            raise ValueError ("Valores inválidos para base e altura")



