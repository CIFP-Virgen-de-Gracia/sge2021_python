from Modulo import Modulo

class ModuloRotacion(Modulo):

    def __init__(self, id, largo, alto, ancho, robot, motor):
        super().__init__(id, largo, alto, ancho, robot)
        if type(motor).__name__ != "MotorRotacion":
            raise ValueError("El motor debe ser de rotacion.")
        self.motor = motor

    @property
    def motor(self):
        return self.__motor

    @motor.setter
    def motor(self, motor):
        self.__motor = motor

    def mover(self):
        self.control.mover()

    def __str__(self):
        clase = type(self).__name__
        msg = "{0} => "+ super().__str__()
        return msg.format(clase)
