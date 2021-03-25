class Sensor():

    def __init__(self, id, tipo):
        self.id = id
        self.tipo = tipo

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, tipo):
        self.__tipo = tipo

    def captar_informacion(self):
        return self.__str__()+" => Capta información de tipo " + self.tipo

    def __str__(self):
        clase = type(self).__name__
        msg = "{0} ID => {1}, TIPO => {2}"
        return msg.format(clase, self.id, self.tipo)