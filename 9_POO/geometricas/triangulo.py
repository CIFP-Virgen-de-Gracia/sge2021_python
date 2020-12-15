from poligono import Poligono

class Triangulo(Poligono):

    def __init__(self, base, altura, *args):
        if len(args) != 3:
            raise ValueError("Un triángulo tiene 3 lados")
        else:
            super().__init__(*args)
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
        """Devuelve el área de un triángulo"""
        return self.base*self.altura/2

