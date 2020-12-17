from ciberpolicia import Ciberpolicia

class CoordinadorPatrulla(Ciberpolicia):
    def __init__(self, id, nombre, nplaca, npatrulla):
        super().__init__(id, nombre, nplaca)
        self.npatrulla = npatrulla
        self.delincuentes = []

    @property
    def npatrulla(self):
        return self.__npatrulla

    @property
    def delincuentes(self):
        return self.__delincuentes

    @delincuentes.setter
    def delincuentes(self, delincuentes):
        self.__delincuentes = delincuentes

    @npatrulla.setter
    def npatrulla(self, npatrulla):
        self.__npatrulla = npatrulla

    def addDelincuente(self, delincuente):
        self.__delincuentes.append(delincuente)

    def getRegistro(self):
        registro = {'patrulla': self.npatrulla, 'delincuente': []}
        for i in self.delincuentes:
            registro.get('delincuente').append(i.getDict())
        return registro
