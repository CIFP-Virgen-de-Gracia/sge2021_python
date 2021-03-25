from Individuo import *
from Sano import *
from datetime import date
import random

class Infectado(Individuo):

    PROB_SUPERAR_ENFERMEDAD_SIN_TRATAMIENTO = 50
    PROB_SUPERAR_ENFERMEDAD_TRATAMIENTO = 90

    def __init__(self, id, nombre, pos_x, oficina, fecha_infeccion):
        super().__init__(id, nombre, pos_x, oficina)
        self.fecha_infeccion = fecha_infeccion
        self.dias_infeccion = 0 # Esta variable la tenemos para incrementar en la simulación y ver el comportamiento
        # cuando hayan pasado los 14 días.
        self.recibe_tratamiento = False
        self.vivo = True

    @property
    def fecha_infeccion(self):
        return self.__fecha_infeccion

    @property
    def dias_infeccion(self):
        return self.__dias_infeccion

    @property
    def recibe_tratamiento(self):
        return self.__recibe_tratamiento

    @property
    def vivo(self):
        return self.__vivo

    @dias_infeccion.setter
    def dias_infeccion(self, dias):
        self.__dias_infeccion = dias

    @fecha_infeccion.setter
    def fecha_infeccion(self, fecha_infeccion):
        self.__fecha_infeccion = fecha_infeccion

    @recibe_tratamiento.setter
    def recibe_tratamiento(self, recibe_tratamiento):
        self.__recibe_tratamiento = recibe_tratamiento

    @vivo.setter
    def vivo(self, vivo):
        self.__vivo = vivo

    def incrementar_dia(self):
        self.__dias_infeccion += 1

    def recibir_tratamiento(self):
        if self.recibe_tratamiento:
            raise ValueError("Ya ha recibido tratamiento anteriormente.")
        self.__recibe_tratamiento = True

    def supera_enfermedad(self):
        """Superará la enfermedad cuando hayan pasado los 14 días en función de si ha recibido
        tratamiento y las probabilidades correspondientes"""
        if self.dias_infeccion < 14:
            raise ValueError("Aún no han pasado 14 días.")

        prob = random.randint(0, 100)
        if self.recibe_tratamiento and prob < 90: # supera la enfermedad
            return True
        if self.recibe_tratamiento and prob >= 90: # no supera la enfermedad
            return False
        if not prob < 50: # supera la enfermedad sin tratamiento
            return True
        return False # No supera la enfermedad sin tratamiento

    def superar_enfermedad(self):
        if not self.vivo:
            raise ValueError("No puede superar la enfermedad, porque este individuo muere.")
        return Sano(self.id, self.nombre, self.pos_x, self.oficina, False, False, True)

    def morir(self):
        self.vivo = False

    def infectar(self, sano):
        """Un individuo infectado puede infectar a uno sano siempre que no sea inmune, esté vacunado o tenga anticuerpos"""
        if sano.inmune:
            raise ValueError("El individuo sano es inmune, no se puede infectar.")
        if sano.tiene_anticuerpos:
            raise ValueError("El individuo sano no se puede reinfectar.")
        if sano.vacunado:
            raise ValueError("El individuo sano está vacunado, no se puede infectar.")
        sano = Infectado(sano.id, sano.nombre, sano.pos_x, sano.oficina, date.today())
        return sano

    def __str__(self):
        clase = type(self).__name__
        msg = super().__str__()+ " => {0} => Fecha_infeccion: {1}, Dias infeccion: {2} => "
        if self.vivo:
            msg += "VIVO"
        else:
            msg += "MUERTO"

        return msg.format(clase, self.fecha_infeccion, self.dias_infeccion)