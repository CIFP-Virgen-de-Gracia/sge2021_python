from Rex import Rex
from Spinosaurus import Spinosaurus
from Triceraptors import Triceraptors
from Aldea import Aldea
import random

class FactoriaAldea:

    def crear_aldea(nombre, num_rex, num_spinosaurus, num_triceraptors):
        a = Aldea(nombre)
        for i in range(num_rex):
            a.add_dinosaurio(Rex("r" + str(i), 1000, random.randrange(-200, 200), a))
        for i in range(num_spinosaurus):
            a.add_dinosaurio(Spinosaurus("s" + str(i), 1000, random.randrange(-200, 200), a))
        for i in range(num_triceraptors):
            a.add_dinosaurio(Triceraptors("t" + str(i), 1000, random.randrange(-200, 200), a))
        return a