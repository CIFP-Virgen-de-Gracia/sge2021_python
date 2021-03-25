class Motor():

    def __init__(self, id):
        self.id = id

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    def __str__(self):
        clase = type(self).__name__
        msg = "{0} ID => {1}, TIPO => {2}"
        return msg.format(clase, self.id, self.tipo)