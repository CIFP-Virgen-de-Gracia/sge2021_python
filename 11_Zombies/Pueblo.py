from Personaje import Personaje
from Humano import Humano

class Pueblo():

    def __init__(self, nombre):
        self.nombre = nombre
        self.personajes = []

    @property
    def personajes(self):
        return self.__personajes

    @property
    def nombre(self):
        return self.__nombre

    @personajes.setter
    def personajes(self, personajes):
        self.__personajes = personajes

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    def add_personaje(self, personaje):
        self.__personajes.append(personaje)

    def hay_supervivientes(self):
        supervivientes = False
        i = 0
        while not supervivientes and i < len(self.personajes):
            p = self.personajes[i]
            if type(p).__name__ == "Humano" and p.vivo:
                supervivientes = True
            i+=1
        return supervivientes

    def ordenar_personajes(self):
        self.__personajes.sort(key= lambda personaje: personaje.pos_x)

    def seleccionar_personaje(self, id, faccion):
        encontrado = False
        i = 0
        while not encontrado and i < len(self.personajes):
            if id == self.personajes[i].id and type(self.personajes[i]).__name__ == faccion:
                encontrado = True
                p = self.personajes[i]
            i+=1
        if not encontrado:
            raise ValueError("Personaje no encontrado.")
        return p

    def comprobar_peligros_cerca(self):
        """Compruea los humanos que tienen zombies cerca"""
        for p in self.personajes:
            if type(p).__name__ == "Humano" and p.vivo:
                self.comprobar_peligro_personaje(p)

    def comprobar_peligro_personaje(self, personaje):
        """Comprueba si el humano tiene zombies cerca para avisarle"""
        peligro = False
        for z in self.personajes:
            if type(z).__name__ == "Zombie" and z.vivo and abs(personaje.pos_x - z.pos_x) <= 5:
                personaje.sentir_peligro_cerca()
                peligro = True
            if not peligro:
                personaje.no_sentir_peligro()

    def actualizar_estado(self):
        """Comprobará el estado de los personajes para desencadenar las acciones correspondientes"""
        # Si un humano tiene un zombie a menos 5 unidades o menos debe indicársele
        self.comprobar_peligros_cerca()

    def get_personajes_posicion(self, pos_x, faccion):
        """Obtenemos los personajes que se encuentran en una posición concreta"""
        n_personaje = 0
        personajes = []
        pos = self.personajes[0].pos_x
        while pos <= pos_x and n_personaje < len(self.personajes):
            personaje = self.personajes[n_personaje]
            if personaje.pos_x == pos_x and type(personaje).__name__ == faccion:
                personajes.append(personaje)
            pos = personaje.pos_x
            n_personaje += 1
        return personajes

    def __str__(self):
        """Mostrará el pueblo ordenando los personajes por posición"""
        self.ordenar_personajes()
        clase = type(self).__name__
        msg = "{0} => Nombre: {1}\nPersonajes: \n"
        for p in self.personajes:
            msg += p.__str__()+"\n"
        return msg.format(clase, self.nombre)