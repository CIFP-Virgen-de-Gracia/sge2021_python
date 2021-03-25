from Control import Control

class Modulo():

    def __init__(self, id, largo, alto, ancho, robot):
        if id < 1 or id > 255:
            raise ValueError("El id debe estar entre 1-255.")
        if largo < 1 or largo > 200 or alto < 1 or alto > 200 or ancho < 1 or ancho > 200:
            raise ValueError("Las dimensiones deben tener un valor comprendido entre 1 y 200mm")

        self.id = id
        self.largo = largo
        self.alto = alto
        self.ancho = ancho
        self.robot = robot
        self.control = Control(self)

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def largo(self):
        return self.__largo

    @largo.setter
    def largo(self, largo):
        self.__largo = largo

    @property
    def alto(self):
        return self.__alto

    @alto.setter
    def alto(self, alto):
        self.__alto = alto

    @property
    def ancho(self):
        return self.__ancho

    @ancho.setter
    def ancho(self, ancho):
        self.__ancho = ancho

    @property
    def control(self):
        return self.__control

    @control.setter
    def control(self, control):
        self.__control = control

    @property
    def robot(self):
        return self.__robot

    @robot.setter
    def robot(self, robot):
        self.__robot = robot

    def __str__(self):
        clase = type(self).__name__
        msg = "{0} ID => {1}, Largo => {2}, Ancho => {3}, Alto => {4}\n"
        msg += self.control.__str__()
        return msg.format(clase, self.id, self.largo, self.ancho, self.alto)