from poligono import Poligono

class Rectangulo(Poligono):

    def __init__(self, base, altura):
            super().__init__(base, base, altura, altura)
            self.base = base
            self.altura = altura

    @property
    def base(self):
        return self.__base

    @property
    def altura(self):
        return self.__altura

    @base.setter
    def base(self, base):
        self.__base = base

    @altura.setter
    def altura(self, altura):
        self.__altura = altura

    def getArea(self):
        """Devuelve el área de un rectángulo"""
        return self.base*self.altura

