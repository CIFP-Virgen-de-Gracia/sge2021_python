from random import choice

class Password():
    def __init__(self, long=8):
        self.longitud = long
        self.generarPassword()

    @property
    def longitud(self):
        return self.__longitud

    @longitud.setter
    def longitud(self, long):
        if long>0:
            self.__longitud = long
        else:
            self.__longitud = 8
            raise ValueError("La longitud tiene que ser positiva mayor que cero")


    @property
    def valor(self):
        return self.__valor

    def __str__(self):
        clase = type(self).__name__
        msg = "{0} de longitud {1} y valor {2}"
        if self.esFuerte():
            msg += " es fuerte"
        else:
            msg += " es débil"
        return msg.format(clase, self.longitud, self.valor)

    def generarPassword(self):
        valores = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ<=>@#%&+"
        self.__valor = "";
        for i in range(self.longitud):
            self.__valor += choice(valores)

    def esFuerte(self):
        """Será fuerte si tiene más 2 mayúsculas, más 1 minúscula y más de 5 números"""
        if len(self.__valor) < 8:
            return False
        else:
            mins = "abcdefghijklmnñopqrstuvwxyz"
            mays = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
            num = "0123456789"
            nmins, nmays, nnums = 0, 0, 0
            for a in self.__valor:
                if a in mins:
                    nmins += 1
                elif a in mays:
                    nmays += 1
                elif a in num:
                    nnums += 1
            if nmays > 2 and nmins > 1 and nnums > 5:
                return True
            else:
                return False




