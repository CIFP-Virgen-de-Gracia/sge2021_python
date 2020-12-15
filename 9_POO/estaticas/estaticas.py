class Alumno():

    def __init__(self, nombre=""):
        self.nombre = nombre

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    def __str__(self):
        return self.nombre

a1 = Alumno("Pepe")
print(a1)



