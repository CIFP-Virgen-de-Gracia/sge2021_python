from persona import Persona

class Delincuente(Persona):
    def __init__(self, id, nombre, actosDelictivos):
        super().__init__(id, nombre)
        self.actosDelictivos = actosDelictivos

    @property
    def actosDelictivos(self):
        return self.__actosDelictivos

    @actosDelictivos.setter
    def actosDelictivos(self, actosDelictivos):
        self.__actosDelictivos = actosDelictivos

    def addDelito(self, delito):
        self.__actosDelictivos.append(delito)

    def getDict(self):
        datos = {'id': self.id, 'nombre': self.nombre, 'delito': self.actosDelictivos}
        return datos;