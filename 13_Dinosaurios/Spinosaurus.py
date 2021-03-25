from Depredador import Depredador
from Constantes import *

class Spinosaurus(Depredador):
    POSIB_ATAQUE = 30
    def __init__(self, id, energia, pos_x, aldea):
        super().__init__(id, energia, pos_x, False, True, aldea)

    def desplazar(self, distancia, direccion):
        super().desplazar(distancia, direccion, 2)

    def recibir_ataque(self, depredador):
        super().recibir_ataque(depredador, POSIB_PRESA_SOLITARIO)

    def elegir_accion(self):
        return super().elegir_accion(self.POSIB_ATAQUE)