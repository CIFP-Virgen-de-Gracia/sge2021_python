# coding=utf-8
from Factorias.FactoriaPatrulla import FactoriaPatrulla
from Utilidades.Utilidades import Utilidades

# Creamos una patrulla con sus ciberpolicías y su coordinador

patrulla = FactoriaPatrulla.crear_patrulla()
registro = patrulla.get_registro()
Utilidades.grabarJSON(registro)