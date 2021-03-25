from Modulo import Modulo

class ModuloEstatico(Modulo):

    def __init__(self, id, largo, alto, ancho, robot, sensores):
        super().__init__(id, largo, alto, ancho, robot)
        self.__comprueba_sensores(len(sensores))
        self.sensores = sensores

    @property
    def sensores(self):
        return self.__sensores

    @sensores.setter
    def sensores(self, sensores):
        self.__comprueba_sensores(len(sensores))
        self.__sensores = sensores

    def add_sensor(self, sensor):
        __comprueba_sensores(len(sensores)+1)
        self.__sensores.append(sensores)

    def captar_informacion(self):
        self.control.captar()

    def __str__(self):
        clase = type(self).__name__
        msg = "{0} => "+ super().__str__()
        return msg.format(clase)

    def __comprueba_sensores(self, n_sensores):
        if n_sensores < 0 or n_sensores > 5:
            raise ValueError("Debe haber entre 0 y 5 sensores")