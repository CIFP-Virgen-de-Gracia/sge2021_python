import json

class Utilidades:

    @staticmethod
    def get_entero(msg):
        """Pide un valor entero por teclado"""
        correcto = False
        valor = 0
        while not correcto:
            try:
                valor = int(input(msg))
                correcto = True
            except ValueError:
                print("El valor de " + msg + " debe ser numérico entero")
        return valor

    @staticmethod
    def grabarJSON(registro):
        nombre = input("Fichero JSON: ")
        fichero = open(nombre, "w")
        json.dump(registro, fichero)
        fichero.close