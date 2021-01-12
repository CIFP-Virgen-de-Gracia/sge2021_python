from Ciberpolicia import *


class FactoriaPolicia():

    @staticmethod
    def crear_policia(id_patrulla):
        """Crea un policía"""
        # Solicitaremos el id, nombre, número de placa
        id = input("Id policía: ")
        nombre = input("Nombre policía: ")
        nPlaca = input("Número de placa: ")
        return Ciberpolicia(id, nombre, nPlaca, id_patrulla)