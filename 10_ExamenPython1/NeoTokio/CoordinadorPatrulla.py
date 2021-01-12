from Ciberpolicia import Ciberpolicia

class CoordinadorPatrulla(Ciberpolicia):
    def __init__(self, id, nombre, n_placa, n_patrulla):
        super().__init__(id, nombre, n_placa, n_patrulla)
        self.delincuentes = []

    @property
    def delincuentes(self):
        return self.__delincuentes

    @delincuentes.setter
    def delincuentes(self, delincuentes):
        self.__delincuentes = delincuentes

    def add_delincuente(self, delincuente):
        self.__delincuentes.append(delincuente)

    def get_registro(self):
        registro = {'patrulla': self.id_patrulla, 'delincuente': []}
        for i in self.delincuentes:
            registro.get('delincuente').append(i.get_dict())
        return registro
