from rectangulo import *

class Cubo():
    def __init__(self, lado):
        self.cuadrado = Rectangulo(lado, lado)

    @property
    def cuadrado(self):
        return self.__cuadrado

    @cuadrado.setter
    def cuadrado(self, cuadrado):
        self.__cuadrado = cuadrado

    def getPerimetro(self):
        return self.cuadrado.base*12

    def getArea(self):
        return self.cuadrado.getArea()*6

    def __str__(self):
        clase = type(self).__name__
        msg = "{0} de lado {1}"
        return msg.format(clase, self.cuadrado.base)
