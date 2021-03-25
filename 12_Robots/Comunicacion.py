class Comunicacion():

    def __init__(self):
        self.mensajes_recibidos = []

    @property
    def mensajes_recibidos(self):
        return self.__mensajes_recibidos

    @mensajes_recibidos.setter
    def mensajes_recibidos(self, mensajes_recibidos):
        self.__mensajes_recibidos = mensajes_recibidos

    def enviar(self, msg, destinatario):
        if type(destinatario).__name__ == "Robot":
            for m in destinatario.modulos:
                self.enviar(msg, m)
        else:
            destinatario.control.comunicacion.recibir(msg)

    def recibir(self, msg):
        self.__mensajes_recibidos.append(msg)

    def __str__(self):
        clase = type(self).__name__
        msg = "{0} \n Mensajes Recibidos: \n"
        for i in self.mensajes_recibidos:
            msg += i+"\n"
        return msg.format(clase)