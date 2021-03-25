# coding=utf-8
from Constantes import *
import random

class Dinosaurio():

    def __init__(self, id, energia, pos_x, manada, alimentacion, bipedo, aldea):
        self.id = id
        self.energia = energia
        self.pos_x = pos_x
        self.aldea = aldea
        self.manada = manada
        self.alimentacion = alimentacion
        self.bipedo = bipedo
        if self.energia > 0:
            self.vivo = True
        else:
            self.vivo = False

    @property
    def id(self):
        return self.__id

    @property
    def energia(self):
        return self.__energia

    @property
    def pos_x(self):
        return self.__posX

    @property
    def manada(self):
        return self.__manada

    @property
    def alimentacion(self):
        return self.__alimentacion

    @property
    def bipedo(self):
        return self.__bipedo

    @property
    def aldea(self):
        return self.__aldea

    @property
    def vivo(self):
        return self.__vivo

    @id.setter
    def id(self, id):
        self.__id = id

    @energia.setter
    def energia(self, energia):
        self.__energia = energia

    @pos_x.setter
    def pos_x(self, pos_x):
        self.__posX = pos_x

    @manada.setter
    def manada(self, manada):
        self.__manada = manada

    @alimentacion.setter
    def alimentacion(self, alimentacion):
        self.__alimentacion = alimentacion

    @bipedo.setter
    def bipedo(self, bipedo):
        self.__bipedo = bipedo

    @aldea.setter
    def aldea(self, aldea):
        self.__aldea = aldea

    @vivo.setter
    def vivo(self, vivo):
        self.__vivo = vivo

    def desplazar(self, distancia, direccion, energia):
        """El personaje se desplaza una distancia en una dirección y consume una cantidad
        de energía"""
        if not self.vivo:
            raise ValueError("Personaje muerto. No se puede desplazar.")
        if self.energia < energia*distancia:
            raise ValueError("Energía insuficiente. No se puede desplazar así.")
        if direccion == DIR_IZQDA:
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

    def morir(self):
        """El personaje muere"""
        self.energia = 0
        self.vivo = False

    def comer(self):
        if not self.vivo:
            raise ValueError("Personaje muerto. No puede comer.")
        self.energia += ENERGIA_COMER

    def recibir_ataque(self, depredador, posibilidades_supervivencia):
        opcion = random.randint(0,100)
        if opcion < posibilidades_supervivencia:
            # Gana la presa, muere el atacante
            depredador.morir()
        else: # Gana el depredador, muere la presa
            self.morir()

    def elegir_accion(self, prob_ataque):
        opcion = random.randint(0, 100)
        opciones_restantes = 100-prob_ataque
        if opcion < prob_ataque:
            return ATACAR
        elif opcion < (opciones_restantes/2): #Nos queda comer y desplazarnos
            return COMER
        else:
            return DESPLAZARSE

    def __str__(self):
        clase = type(self).__name__
        msg = "{0} => ID: {1}, Energía: {2}, Posición: {3}, "
        if self.manada:
            msg += "Manada, "
        else:
            msg += "Solitario, "

        if self.bipedo:
            msg += "Bípedo, "
        else:
            msg += "No es bípedo, "

        msg += "Alimentacion: {4} => "
        if self.vivo:
            msg += "VIVO"
        else:
            msg += "MUERTO"


        return msg.format(clase, self.id, self.energia, self.pos_x, self.alimentacion)
