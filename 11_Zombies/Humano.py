from Personaje import Personaje

class Humano(Personaje):

    def __init__(self, id, nombre, energia, pos_x, pueblo):
        super().__init__(id, nombre, energia, pos_x, pueblo)
        self.necesita_ayuda = False

    @property
    def necesita_ayuda(self):
        return self.__necesita_ayuda

    @necesita_ayuda.setter
    def necesita_ayuda(self, value):
        self.__necesita_ayuda = value

    def caminar(self, direccion):
        super().desplazar(10, direccion, 5)

    def correr(self, direccion):
        super().desplazar(40, direccion, 60)

    def trotar(self, direccion):
        super().desplazar(20, direccion, 15)

    def atacar(self, personaje):
        """Un humano puede atacar a otro personaje si está en la misma posición. Consume 10 puntos
        de energía y el atacado se resta 100 al recibir el ataque"""
        if not self.vivo:
            raise ValueError("Personaje muerto. No puede atacar.")
        if self.pos_x != personaje.pos_x:
            raise ValueError("Distinta posición. No puede atacarle.")
        if self.energia < 10:
            raise ValueError("Energía insuficiente. No puede atacar")

        personaje.recibir_ataque(self);
        self.energia -= 10
        if self.energia == 0:
            self.morir()

    def sentir_peligro_cerca(self):
        """Se notifica al humano que tiene zombies cerca"""
        self.pedir_ayuda()

    def no_sentir_peligro(self):
        """El peligro inminente ha desaparecido"""
        self.necesita_ayuda = False

    def pedir_ayuda(self):
        """Activará la propiedad necesita ayuda a True.
        Consumo de energía de 5 unidades"""
        if not self.vivo:
            raise ValueError("Personaje muerto. No puede pedir ayuda")
        if self.energia < 5:
            raise ValueError("Insuficiente energía. No puede pedir ayuda")
        self.energia -= 5
        self.necesita_ayuda = True
        if self.energia == 0:
            self.morir()

    def recibir_grito(self):
        """A los humanos no les afectan los gritos"""
        if not self.vivo:
            raise ValueError("Personaje muerto. Le da igual que le griten.")

    def __str__(self):
        clase = type(self).__name__
        vivo = "VIVO"
        peligro = "EN PELIGRO"
        if not self.vivo:
            vivo = "MUERTO"

        if not self.necesita_ayuda:
            peligro = ""

        msg = super().__str__()+ " => {0} => {1} {2}\nPerseguidores: "
        for i in self.perseguidores:
            msg += i.id + " "
        return msg.format(clase, vivo, peligro)

