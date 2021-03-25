from Modulo import Modulo

class Robot():

    def __init__(self, modulos):
        self.modulos = modulos

    @property
    def modulos(self):
        return self.__modulos

    @modulos.setter
    def modulos(self, modulos):
        self.__modulos = modulos

    def __str__(self):
        clase = type(self).__name__
        msg = "{0} MÓDULOS => \n"
        for modulo in self.modulos:
            msg += modulo.__str__() + "\n"
        return msg.format(clase)