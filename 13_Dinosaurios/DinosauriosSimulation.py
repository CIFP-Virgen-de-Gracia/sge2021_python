from Factorias.FactoriaAldea import FactoriaAldea
from Constantes import *
import random

def elegir_dinosaurio_distinto(aldea, dinosaurio):
    encontrado = False
    i = 0
    d = None
    while not encontrado and i < len(aldea.dinosaurios):
        d = aldea.dinosaurios[i]
        if dinosaurio.id != d.id and d.vivo:
            encontrado = True
        else:
            i += 1
    if not encontrado:
        d = None
    return d

def simular_dinosaurios(aldea):
    for dinosaurio in aldea.dinosaurios:
        if dinosaurio.vivo:
            opcion = dinosaurio.elegir_accion()
            if opcion == ATACAR:
                # Elegimos el dinosaurio al cual atacar
                presa = elegir_dinosaurio_distinto(aldea, dinosaurio)
                if presa != None:
                    print(dinosaurio.id + " ataca a " + presa.id)
                    dinosaurio.atacar(presa)
                else:
                    print(dinosaurio.id + " quiere atacar pero no hay presas.")
            elif opcion == COMER:
                print(dinosaurio.id + " come")
                dinosaurio.comer()
            elif opcion == DESPLAZARSE:
                # Tenemos que elegir la dirección y las unidades
                dir = random.randint(0,2)
                unidades = random.randint(1,20)
                if dir == 0: #Derecha
                    print(dinosaurio.id + " se desplaza " + str(unidades) + " ud a la derecha")
                    dinosaurio.desplazar(unidades, DIR_DCHA)
                else:
                    print(dinosaurio.id + " se desplaza " + str(unidades) + " ud a la izquierda")
                    dinosaurio.desplazar(unidades, DIR_IZQDA)


# Comienza flujo del programa
aldea = FactoriaAldea.crear_aldea("Puertollano", 20, 15, 15)
parar = "N"
# Mientras el usuario no pare la simulación
while (parar != "S" or parar != "s") and aldea.hay_depredadores():
    # Mostramos situación actual
    print(aldea)
    # Cada dinosaurio realizará una acción
    simular_dinosaurios(aldea)
    parar = input("Desea parar (S/N): ")

print(aldea)
if not aldea.hay_depredadores():
    print("No hay depredadores.")


