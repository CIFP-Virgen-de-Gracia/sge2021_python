from persona import Persona

class Ciberpolicia(Persona):

    def __init__(self, id, nombre, nplaca):
        super().__init__(id, nombre)
        self.nplaca = nplaca

    @property
    def nplaca(self):
        return self.__nplaca

    @nplaca.setter
    def nplaca(self, nplaca):
        self.__nplaca = nplaca

    def __str__(self):
        clase = type(self).__name__
        msg = super().__str__()+" {0} => Número de placa: {1}"
        return msg.format(clase, self.nplaca)