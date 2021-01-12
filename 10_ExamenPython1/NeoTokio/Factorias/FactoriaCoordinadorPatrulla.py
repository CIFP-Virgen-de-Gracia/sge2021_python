from CoordinadorPatrulla import CoordinadorPatrulla
from Factorias.FactoriaDelincuente import FactoriaDelincuente
from Utilidades.Utilidades import Utilidades


class FactoriaCoordinadorPatrulla:

    @staticmethod
    def crear_coordinador(id_patrulla):
        """Crea un coordinador de patrulla"""
        # Solicitamos el id_coordinador, nombre, número de placa
        id_coordinador = input("Id del coordinador: ")
        nombre = input("Nombre del coordinador: ")
        n_placa = input("Número de placa: ")
        coordinador = CoordinadorPatrulla(id_coordinador, nombre, n_placa, id_patrulla)
        coordinador.delincuentes = FactoriaCoordinadorPatrulla.crear_delincuentes()
        return coordinador

    @staticmethod
    def crear_delincuentes():
        """Obtenemos una lista de delincuentes para registrar"""
        n = Utilidades.get_entero("Número de delincuentes: ")
        delincuentes = []
        for i in range(n):
            delincuentes.append(FactoriaDelincuente.crear_delincuente())
        return delincuentes
