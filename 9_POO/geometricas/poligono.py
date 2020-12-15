class Poligono():
    def __init__(self, *args):
        self.lados = args
        self.__nlados=len(self.lados)

    @property
    def lados(self):
        return self.__lados

    @lados.setter
    def lados(self, lados):
        self.__lados = lados

    @property
    def nlados(self):
        return self.__nlados


    def __str__(self):
        clase = type(self).__name__
        msg = "{0} de {1} lados con longitudes {2}"
        return msg.format(clase, self.nlados, self.lados)

    def getPerimetro(self):
        """Devuelve el perímetro del polígono"""
        return sum(self.lados)

