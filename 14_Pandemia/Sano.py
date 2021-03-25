from Individuo import *

class Sano(Individuo):

    def __init__(self, id, nombre, pos_x, oficina, inmune, vacunado, tiene_anticuerpos):
        super().__init__(id, nombre, pos_x, oficina)
        self.inmune = inmune
        self.vacunado = vacunado
        self.tiene_anticuerpos = tiene_anticuerpos

    @property
    def inmune(self):
        return self.__inmune

    @property
    def vacunado(self):
        return self.__vacunado

    @property
    def tiene_anticuerpos(self):
        return self.__tiene_anticuerpos

    @inmune.setter
    def inmune(self, inmune):
        self.__inmune = inmune

    @vacunado.setter
    def vacunado(self, vacunado):
        self.__vacunado = vacunado

    @tiene_anticuerpos.setter
    def tiene_anticuerpos(self, tiene_anticuerpos):
        self.__tiene_anticuerpos = tiene_anticuerpos

    def ser_vacunado(self):
        """El individuo sano recibe la vacuna"""
        if self.tiene_anticuerpos:
            raise ValueError("No puede ser vacunado, ha pasado la enfermedad.")
        if self.inmune:
            raise ValueError("No puede ser vacunado, es inmune.")
        if self.vacunado:
            raise ValueError("No puede ser vacunado, ya lo está.")

        self.vacunado = True

    def __str__(self):
        clase = type(self).__name__
        msg = super().__str__()+ " => {0} =>"
        if self.vacunado:
            msg += " VACUNADO "
        if self.tiene_anticuerpos:
            msg += " CON ANTICUERPOS "
        if self.inmune:
            msg += " INMUNE"

        return msg.format(clase)


