from Factorias.FactoriaCoordinadorPatrulla import FactoriaCoordinadorPatrulla
from Factorias.FactoriaPolicia import FactoriaPolicia
from Patrulla import Patrulla
from Utilidades.Utilidades import Utilidades


class FactoriaPatrulla:

    @staticmethod
    def crear_patrulla():
        """Crea una patrulla"""
        # Solicitamos el id de la patrulla
        # Solicitamos los datos del coordinador de patrulla
        # Solicitamos los datos del resto de policías
        id = input("Id de la patrulla: ")
        coordinador = FactoriaCoordinadorPatrulla.crear_coordinador(id)
        correcto = False
        while not correcto:
            try:
                ciberpolicias = FactoriaPatrulla.crear_ciberpolicias(id)
                p = Patrulla(id, coordinador, ciberpolicias)
                correcto = True
            except ValueError:
                print("Debes introducir al menos 4 ciberpolicías")
        return p

    @staticmethod
    def crear_ciberpolicias(id):
        """Crea la lista de ciberpolicias que formarán una patrulla"""
        nPolicias = Utilidades.get_entero("Número de ciberpolicías: ")
        ciberpolicias = []
        for i in range(nPolicias):
            ciberpolicias.append(FactoriaPolicia.crear_policia(id))
        return ciberpolicias

