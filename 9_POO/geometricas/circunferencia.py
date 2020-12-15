import math

class Circunferencia():

    def __init__(self, radio):
        self.radio = radio

    @property
    def radio(self):
        return self.__radio

    @radio.setter
    def radio(self, radio):
        self.__radio = radio

    def getArea(self):
        return self.radio*math.pi**2

    def getPerimetro(self):
        return self.radio*2*math.pi

    def __str__(self):
        clase = type(self).__name__
        msg = "{0} de radio {1}"
        return msg.format(clase, self.radio)
