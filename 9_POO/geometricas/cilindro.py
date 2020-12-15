from circunferencia import *
from rectangulo import *
import math

class Cilindro():
    def __init__(self, radio, altura):
        self.circunferencia = Circunferencia(radio)
        self.rectangulo = Rectangulo(2*math.pi*radio, altura)

    @property
    def circunferencia(self):
        return self.__circunferencia

    @property
    def rectangulo(self):
        return self.__rectangulo

    @circunferencia.setter
    def circunferencia(self, circunferencia):
        self.__circunferencia = circunferencia

    @rectangulo.setter
    def rectangulo(self, rectangulo):
        self.__rectangulo = rectangulo

    def getPerimetro(self):
        return self.circunferencia.getPerimetro()*2+self.rectangulo.altura

    def getArea(self):
        return self.circunferencia.getArea()*2+self.rectangulo.getArea()

    def __str__(self):
        clase = type(self).__name__
        msg = "{0} de radio {1} y altura {2}"
        return msg.format(clase, self.circunferencia.radio, self.rectangulo.altura)
