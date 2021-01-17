class Persona():
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre

    @property
    def id(self):
        return self.__id

    @property
    def nombre(self):
        return self.__nombre

    @id.setter
    def id(self, id):
        self.__id = id

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    def __str__(self):
        clase = type(self).__name__
        msg = "{0} => ID: {1}, Nombre: {2}"
        return msg.format(clase, self.id, self.nombre)
