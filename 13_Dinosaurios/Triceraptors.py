from Dinosaurio import Dinosaurio
from Constantes import *
import random

class Triceraptors(Dinosaurio):

    POSIB_ATAQUE=0
    def __init__(self, id, energia, pos_x, aldea):
        super().__init__(id, energia, pos_x, True, HERBIVORO, False, aldea)

    def desplazar(self, distancia, direccion):
        super().desplazar(distancia, direccion, 5)

    def recibir_ataque(self, depredador):
        # Cuando un Triceraptors recibe un ataque, al ser presa y estar en manada,
        # tendrá 800% posibilidades de sobrevivir
        super().recibir_ataque(depredador, POSIB_PRESA_MANADA)

    def elegir_accion(self):
        return super().elegir_accion(self.POSIB_ATAQUE)