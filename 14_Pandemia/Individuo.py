from Constantes import *

class Individuo():

    def __init__(self, id, nombre, pos_x, oficina):
        self.id = id
        self.nombre = nombre
        self.pos_x = pos_x
        self.oficina = oficina

    @property
    def id(self):
        return self.__id

    @property
    def nombre(self):
        return self.__nombre

    @property
    def pos_x(self):
        return self.__posX

    @property
    def oficina(self):
        return self.__oficina

    @id.setter
    def id(self, id):
        self.__id = id

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @pos_x.setter
    def pos_x(self, pos_x):
        self.__posX = pos_x

    @oficina.setter
    def oficina(self, oficina):
        self.__oficina = oficina

    def desplazar(self, distancia, direccion):
        """El individuo se desplaza una distancia en una dirección"""
        if direccion == DIR_IZQDA:
            self.pos_x -= distancia
        else:
            self.pos_x += distancia

        # No permitimos salirnos del límite -200, 200
        if self.pos_x < -20:
            self.pos_x = -20
        if self.pos_x > 20:
            self.pos_x = 20

    def __str__(self):
        clase = type(self).__name__
        msg = "{0} => ID: {1}, Nombre: {2}, Posición: {3}"

        return msg.format(clase, self.id, self.nombre, self.pos_x)
