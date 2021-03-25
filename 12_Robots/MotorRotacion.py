from Motor import Motor

class MotorRotacion(Motor):

    UNIDADES_ROTACION = 10

    def __init__(self, id):
        super().__init__(id)
        self.angulo = 0

    @property
    def angulo(self):
        return self.__angulo

    @angulo.setter
    def angulo(self, angulo):
        self.__angulo = angulo

    def funcionar(self):
        self.angulo += self.UNIDADES_ROTACION
        self.angulo %= 360
        return self.__str__() + " => Rotado"


    def __str__(self):
        clase = type(self).__name__
        msg = "{0} ID => {1}, ANGULO ROTACIÓN => {2}"
        return msg.format(clase, self.id, self.angulo)