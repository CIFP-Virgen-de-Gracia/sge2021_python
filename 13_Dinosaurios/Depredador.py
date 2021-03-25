from Dinosaurio import Dinosaurio
from Constantes import *

class Depredador(Dinosaurio):

    def __init__(self, id, energia, pos_x, manada, bipedo, aldea):
        super().__init__(id, energia, pos_x, manada, CARNIVORO, bipedo, aldea)

    def atacar(self, presa):
        if not self.vivo:
            raise ValueError("No puede atacar. Está muerto")
        if self.energia < ENERGIA_ATACAR:
            raise ValueError("No puede atacar. Energía insuficiente")
        # Calculamos la energía necesaria para desplazarse a su objetivo
        distancia = self.pos_x-presa.pos_x
        energia_necesaria = abs(distancia)*2+ENERGIA_ATACAR
        if self.energia < energia_necesaria:
            raise ValueError("No puede atacar. Energía insuficiente. Necesita: "+
                             energia_necesaria+", Tiene: "+self.energia)

        if distancia < 0: # Nos desplazamos a la izquierda
            self.desplazar(abs(distancia), DIR_IZQDA)
        else:
            self.desplazar(abs(distancia), DIR_DCHA)
        # Gastamos la energía del ataque
        self.energia -= 20

        #La presa recibe el ataque
        presa.recibir_ataque(self)

    def recibir_ataque(self, depredador, posibilidades_sobrevivir):
        super().recibir_ataque(depredador, posibilidades_sobrevivir)

