from Comunicacion import Comunicacion

class Control():

    def __init__(self, modulo):
        self.comunicacion = Comunicacion()
        self.modulo = modulo

    @property
    def comunicacion(self):
        return self.__comunicacion

    @comunicacion.setter
    def comunicacion(self, comunicacion):
        self.__comunicacion = comunicacion

    @property
    def modulo(self):
        return self.__modulo

    @modulo.setter
    def modulo(self, modulo):
        self.__modulo = modulo

    def mover(self):
        if (type(self.modulo).__name__ == "ModuloTraslacion") or (type(self.modulo).__name__ == "ModuloRotacion"):
            msg = self.modulo.motor.funcionar()
        else: #Helicoidal
            for m in self.modulo.motores:
                msg += m.funcionar()
        self.comunicacion.enviar(msg, self.modulo.robot)
        # Lo comunicamos al resto de módulos del robot


    def captar(self):
        msg = "{0} => Captando información sensores: "
        for i in self.modulo.sensores:
            msg += i.captar_informacion() + "\n"
        msg = msg.format(self.modulo.id)
        self.comunicacion.enviar(msg, self.modulo.robot)
        # Lo comunicamos al resto de módulos del robot



    def __str__(self):
        clase = type(self).__name__
        msg = "{0} => {1}"
        return msg.format(clase, self.comunicacion.__str__())