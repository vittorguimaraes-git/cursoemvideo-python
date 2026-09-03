class Termostato:

    def __init__(self):

        self.__temperatura = 24

    @property
    def temperatura(self) -> float:
        return self.__temperatura

    @temperatura.setter
    def temperatura(self, temp) -> None:
        if 16 <= temp <= 30 and temp % 0.5 == 0:
            self.__temperatura = temp
        if temp > 30:
            self.__temperatura = 30

        if temp < 16:
            self.__temperatura = 16




    @property
    def ftemperatura(self) -> str:
        return f"{self.__temperatura}°C"