# coding=utf-8
class Personaje():

    # Algunos valores están fijos como el límite de desplazamiento. Debería ser parametrizable pero para el ejemplo se deja así
    # La dirección también debería ser parametrizable
    def __init__(self, id, nombre, energia, pos_x, pueblo):
        self.id = id
        self.nombre = nombre
        self.energia = energia
        self.pos_x = pos_x
        self.pueblo = pueblo
        self.perseguidores = []
        if self.energia > 0:
            self.vivo = True
        else:
            self.vivo = False

    @property
    def id(self):
        return self.__id

    @property
    def nombre(self):
        return self.__nombre

    @property
    def energia(self):
        return self.__energia

    @property
    def pos_x(self):
        return self.__posX

    @property
    def pueblo(self):
        return self.__pueblo

    @property
    def vivo(self):
        return self.__vivo

    @property
    def perseguidores(self):
        return self.__perseguidores

    @id.setter
    def id(self, id):
        self.__id = id

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @energia.setter
    def energia(self, energia):
        self.__energia = energia

    @pos_x.setter
    def pos_x(self, pos_x):
        self.__posX = pos_x

    @pueblo.setter
    def pueblo(self, pueblo):
        self.__pueblo = pueblo

    @vivo.setter
    def vivo(self, vivo):
        self.__vivo = vivo

    @perseguidores.setter
    def perseguidores(self, perseguidores):
        self.__perseguidores = perseguidores

    def desplazar(self, distancia, direccion, energia):
        """El personaje se desplaza una distancia en una dirección y consume una cantidad
        de energía"""
        if not self.vivo:
            raise ValueError("Personaje muerto. No se puede desplazar.")
        if self.energia < energia:
            raise ValueError("Energía insuficiente. No se puede desplazar así.")
        if direccion == "IZQDA":
            self.pos_x -= distancia
        else:
            self.pos_x += distancia

        # No permitimos salirnos del límite -200, 200
        if self.pos_x < -200:
            self.pos_x = -200
        if self.pos_x > 200:
            self.pos_x = 200

        self.energia -= energia
        if self.energia == 0:
            self.morir()

    def gritar(self):
        """El personaje va a gritar, le afectará a todos los perseguidores que sean zombies."""
        if not self.vivo:
            raise ValueError("Personaje muerto. No puede gritar.")
        if self.energia < 10:
            raise ValueError("Energía insuficiente. No puede gritar.")

        for perseguidor in self.perseguidores:
            perseguidor.recibir_grito()

        self.energia -= 10
        if self.energia == 0:
            self.morir()

    def morir(self):
        """El personaje muere y se notifica al pueblo"""
        self.energia = 0
        self.vivo = False

    def recibir_ataque(self):
        """El personaje recibe el ataque y se le restan 100 puntos de energía"""
        if not self.vivo:
            raise ValueError("Personaje ya muerto.")
        if self.energia >= 100:
            self.energia -= 100
        else:
            self.energia = 0
        if self.energia == 0:
            self.morir()

    def perseguir(self, personaje):
        """En un momento determinado sólo podemos perseguir a un personaje"""
        personaje.ser_perseguido(self)

    def ser_perseguido(self, personaje):
        """Podemos ser perseguidos por varios personajes"""
        if personaje not in self.__perseguidores:
            self.__perseguidores.append(personaje)

    def dejar_de_perseguir(self, personaje):
        personaje.dejar_de_ser_perseguido_por(self)

    def dejar_de_ser_perseguido_por(self, personaje):
        for p in self.__perseguidores:
            if personaje.id == p.id:
                self.__perseguidores.remove(p)

    def __str__(self):
        clase = type(self).__name__

        msg = "{0} => ID: {1}, Nombre: {2}, Energía: {3}, Posición: {4}"
        return msg.format(clase, self.id, self.nombre, self.energia, self.pos_x)