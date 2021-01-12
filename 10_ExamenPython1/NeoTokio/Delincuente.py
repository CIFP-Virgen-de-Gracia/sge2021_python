from Persona import Persona


class Delincuente(Persona):
    def __init__(self, id, nombre, actos_delictivos):
        super().__init__(id, nombre)
        self.actos_delictivos = actos_delictivos

    @property
    def actos_delictivos(self):
        return self.__actos_delictivos

    @actos_delictivos.setter
    def actos_delictivos(self, actos_delictivos):
        self.__actos_delictivos = actos_delictivos

    def add_delito(self, delito):
        self.__actos_delictivos.append(delito)

    def get_dict(self):
        """Obtiene un diccionario con los datos del delincuente"""
        datos = {'id': self.id, 'nombre': self.nombre, 'delito': self.actos_delictivos}
        return datos
