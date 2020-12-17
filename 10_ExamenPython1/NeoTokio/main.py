from patrulla import *
from delincuente import *
import json

def getValorEntero(msg):
    """Pide un valor entero por teclado"""
    correcto = False
    while not correcto:
        try:
            valor = int(input(msg))
            correcto = True
        except ValueError:
            print("El valor de " + msg + " debe ser numérico entero")
    return valor

def crearPatrulla():
    """Crea una patrulla"""
    # Solicitamos el id de la patrulla
    # Solicitamos los datos del coordinador de patrulla
    # Solicitamos los datos del resto de policías
    id = input("Id de la patrulla: ")
    coordinador = getCoordinadorPatrulla(id)
    correcto = False
    while not correcto:
        try:
            ciberpolicias = getCiberpolicias()
            p = Patrulla(id, coordinador, ciberpolicias)
            correcto = True
        except ValueError:
            print("Debes introducir al menos 4 ciberpolicías")
    return p

def getCoordinadorPatrulla(idPatrulla):
    """Crea un coordinador de patrulla"""
    # Solicitamos el id, nombre, número de placa
    id = input("Id del coordinador: ")
    nombre = input("Nombre del coordinador: ")
    nPlaca = input("Número de placa: ")
    return CoordinadorPatrulla(id, nombre, nPlaca, idPatrulla)

def getCiberpolicias():
    """Crea la lista de ciberpolicias que formarán una patrulla"""
    nPolicias = getValorEntero("Número de ciberpolicías: ")
    ciberpolicias = []
    for i in range(nPolicias):
        ciberpolicias.append(getPolicia())
    return ciberpolicias

def getPolicia():
    """Crea un policía"""
    # Solicitaremos el id, nombre, número de placa
    id = input("Id policía: ")
    nombre = input("Nombre policía: ")
    nPlaca = input("Número de placa: ")
    return Ciberpolicia(id, nombre, nPlaca)

def getDelincuente():
    """Crea un delincuente"""
    id = input("Id del delincuente: ")
    nombre = input("Nombre del delincuente: ")
    n = getValorEntero("Número de delitos: ")
    delitos = []
    for i in range(n):
        delitos.append(input("Delito: "))
    return Delincuente(id, nombre, delitos)

def crearDelincuentes():
    """Obtenemos una lista de delincuentes para registrar"""
    n = getValorEntero("Número de delincuentes: ")
    delincuentes = []
    for i in range(n):
        delincuentes.append(getDelincuente())
    return delincuentes

def grabarJSON(registro):
    nombre = input("Fichero JSON: ")
    fichero = open(nombre, "w")
    json.dump(registro, fichero)
    fichero.close

# Creamos una patrulla con sus ciberpolicías y su coordinador
patrulla = crearPatrulla()
delincuentes = crearDelincuentes()
patrulla.coordinadorpatrulla.delincuentes = delincuentes
registro = patrulla.coordinadorpatrulla.getRegistro()
grabarJSON(registro)