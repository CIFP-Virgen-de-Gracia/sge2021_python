from Motor import Motor

class MotorTraslacion(Motor):

    UNIDADES_DESPLAZAMIENTO: int = 10

    def __init__(self, id):
        super().__init__(id)
        self.pos_x = 0

    @property
    def pos_x(self):
        return self.__pos_x

    @pos_x.setter
    def pos_x(self, pos_x):
        self.__pos_x = pos_x

    def funcionar(self):
        self.pos_x += self.UNIDADES_DESPLAZAMIENTO
        return self.__str__() + " => Desplazado"


    def __str__(self):
        clase = type(self).__name__
        msg = "{0} ID => {1}, POSICION => {2}"
        return msg.format(clase, self.id, self.pos_x)