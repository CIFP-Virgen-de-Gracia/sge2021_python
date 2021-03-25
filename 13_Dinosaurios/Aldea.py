
class Aldea():

    def __init__(self, nombre):
        self.nombre = nombre
        self.dinosaurios = []

    @property
    def dinosaurios(self):
        return self.__dinosaurios

    @property
    def nombre(self):
        return self.__nombre

    @dinosaurios.setter
    def dinosaurios(self, dinosaurios):
        self.__dinosaurios = dinosaurios

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    def add_dinosaurio(self, dinosaurio):
        self.__dinosaurios.append(dinosaurio)

    def hay_depredadores(self):
        depredadores = False
        i = 0
        while not depredadores and i < len(self.dinosaurios):
            d = self.dinosaurios[i]
            if d.vivo and (type(d).__name__ == "Rex" or type(d).__name__ == "Spinosaurus"):
                depredadores = True
            i+=1
        return depredadores

    def ordenar_dinosaurios(self):
        self.__dinosaurios.sort(key= lambda dinosaurio: dinosaurio.pos_x)

    def seleccionar_dinosaurio(self, id):
        encontrado = False
        i = 0
        while not encontrado and i < len(self.dinosaurios):
            if id == self.dinosaurios[i].id:
                encontrado = True
                d = self.dinosaurios[i]
            i+=1
        if not encontrado:
            raise ValueError("Dinosaurio no encontrado.")
        return d

    def __str__(self):
        """Mostrará el pueblo ordenando los dinosaurios por posición"""
        self.ordenar_dinosaurios()
        clase = type(self).__name__
        msg = "{0} => Nombre: {1}\nDinosaurios: \n"
        for p in self.dinosaurios:
            msg += p.__str__()+"\n"
        return msg.format(clase, self.nombre)