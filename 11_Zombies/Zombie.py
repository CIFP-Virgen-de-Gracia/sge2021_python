from Personaje import Personaje

class Zombie(Personaje):

    def __init__(self, id, nombre, energia, pos_x, pueblo):
        super().__init__(id, nombre, energia, pos_x, pueblo)

    def caminar(self, direccion):
        super().desplazar(5, direccion, 5)

    def correr(self, direccion):
        super().desplazar(20, direccion, 60)

    def trotar(self, direccion):
        super().desplazar(10, direccion, 15)

    def recibir_grito(self):
        """El zombie recibe un grito y si está vivo se resta 100 de energía"""
        if self.vivo:
            if self.energia > 100:
                self.energia -= 100;
            else:
                self.morir()
        else:
            raise ValueError("El personaje está muerto. Le da igual que le griten.")

    def morder(self, personaje):
        """Sólo los zombies pueden morder a un personaje. Si es humano se convertirá en zombie"""
        if not self.vivo:
            raise ValueError("Personaje muerto. No puede morder.")
        if self.energia < 10:
            raise ValueError("Energía insuficiente. No puede morder.")
        personaje = Zombie(personaje.id, personaje.nombre, personaje.energia, personaje.pos_x, self.pueblo)
        self.energia -= 10
        if self.energia == 0:
            self.morir()
        return personaje

    def __str__(self):
        clase = type(self).__name__
        vivo = "VIVO"
        if not self.vivo:
            vivo = "MUERTO"
        msg = super().__str__()+ " => {0} => {1}"
        return msg.format(clase, vivo)