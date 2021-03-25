from Sano import Sano
from Infectado import Infectado
from Oficina import Oficina
from datetime import date
import random

class FactoriaOficina:

    def crear_oficina(nombre, num_sanos, num_infectados):
        o = Oficina(nombre)
        for i in range(num_sanos):
            o.add_individuo(Sano("s" + str(i), "sano" + str(i), random.randrange(-20, 20), o, random.choice([True, False]), False, False))
        for i in range(num_infectados):
            o.add_individuo(Infectado("i" + str(i), "infectado" + str(i), random.randrange(-20,20), o, date.today()))
        return o