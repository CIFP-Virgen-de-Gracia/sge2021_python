from Modulo import Modulo

class ModuloHelicoidal(Modulo):

    def __init__(self, id, largo, alto, ancho, robot, motores):
        super().__init__(id, largo, alto, ancho, robot)
        if len(motores) != 2:
            raise ValueError("El número de motores debe ser dos.")
        self.motores = motores

    @property
    def motores(self):
        return self.__motores

    @motores.setter
    def motores(self, motores):
        self.__motores = motores

    def mover(self):
        self.control.mover()

    def __str__(self):
        clase = type(self).__name__
        msg = "{0} => "+ super().__str__()
        return msg.format(clase)
