from Humano import Humano
from Zombie import Zombie
from Pueblo import Pueblo
import random

class FactoriaPueblo:

    def crear_pueblo(nombre, num_zombies, num_humanos):
        p = Pueblo(nombre)
        for i in range(num_zombies):
            p.add_personaje(Zombie("z" + str(i), "zombie" + str(i), 1000, random.randrange(-200, 200), p))
        for i in range(num_humanos):
            p.add_personaje(Humano("h" + str(i), "humano" + str(i), 1000, 0, p))
        return p