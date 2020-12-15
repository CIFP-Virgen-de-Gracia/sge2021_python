from circunferencia import *
import math

class Cono():
    def __init__(self, radio, generatriz):
        self.circunferencia = Circunferencia(radio)
        self.generatriz = generatriz

    @property
    def circunferencia(self):
        return self.__circunferencia

    @property
    def generatriz(self):
        return self.__generatriz

    @circunferencia.setter
    def circunferencia(self, circunferencia):
        self.__circunferencia = circunferencia

    @generatriz.setter
    def generatriz(self, generatriz):
        self.__generatriz = generatriz

    def getPerimetro(self):
        return self.circunferencia.getPerimetro()+self.generatriz*2

    def getArea(self):
        return self.circunferencia.getArea()+math.pi*self.circunferencia.radio*self.generatriz

    def __str__(self):
        clase = type(self).__name__
        msg = "{0} de radio {1} y generatriz {2}"
        return msg.format(clase, self.circunferencia.radio, self.generatriz)