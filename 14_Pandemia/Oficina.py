from Sano import *
class Oficina():

    def __init__(self, nombre):
        self.nombre = nombre
        self.individuos = []

    @property
    def individuos(self):
        return self.__individuos

    @property
    def nombre(self):
        return self.__nombre

    @individuos.setter
    def individuos(self, individuos):
        self.__individuos = individuos

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    def add_individuo(self, individuo):
        self.__individuos.append(individuo)

    def hay_posibilidad_infeccion(self):
        """Este método devuelve si puede haber o no nuevas infecciones en la oficina,
        para ello comprueba que haya individuos sanos no inmunes, no vacunados y que no hayan pasado previamente
        la enfermedad"""
        posibles_infectados = False
        i = 0
        while not posibles_infectados and i < len(self.individuos):
            p = self.individuos[i]
            if type(p).__name__ == "Sano" and not p.inmune and not p.vacunado and not p.tiene_anticuerpos:
                posibles_infectados = True
            i+=1
        return posibles_infectados

    def ordenar_individuos(self):
        self.__individuos.sort(key= lambda individuo: individuo.pos_x)

    def extender_infeccion(self):
        """Compruea los individuos que están a 1 m o menos de un infectado y que se puedan infectar, en este caso, se infectan"""
        for p in self.individuos:
            if type(p).__name__ == "Infectado":
                self.infectar_posibles_victimas(p)

    def infectar_posibles_victimas(self, infectado):
        """Comprueba si el infectado tiene cerca posibles individuos sanos que puedan ser infectados,
        en cuyo casoo se infectan"""
        for z in self.individuos:
            if type(z).__name__ == "Sano" and not z.vacunado and not z.inmune and not z.tiene_anticuerpos and abs(infectado.pos_x - z.pos_x) <= 1:
                index = self.individuos.index(z)
                self.individuos[index] = infectado.infectar(z)

    def actualizar_sanos(self):
        """Comprueba los individuos que superan la enfermedad porque ya hayan pasado los 14 días y por probabilidad la
        superen o mueran en función de las posibilidades en cada caso"""
        for p in self.individuos:
            if type(p).__name__ == "Infectado" and p.dias_infeccion >= 14 and p.vivo:
                if not p.supera_enfermedad():
                    p.morir()
                else:
                    index = self.individuos.index(p)
                    self.individuos[index] = p.superar_enfermedad()

    def __str__(self):
        """Mostrará el pueblo ordenando los individuos por posición"""
        self.ordenar_individuos()
        clase = type(self).__name__
        msg = "{0} => Nombre: {1}\nIndividuos: \n"
        for p in self.individuos:
            msg += p.__str__()+"\n"
        return msg.format(clase, self.nombre)