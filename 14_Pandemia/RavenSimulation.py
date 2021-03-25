from Factorias.FactoriaOficina import FactoriaOficina
from Constantes import *
import random


def realizar_acciones_simulacion(oficina):
    # Vamos a realizar los desplazamientos aleatoriamente e incrementaremos el tiempo para los infectados
    # en una semana
    #También decidiremos si un infectado recibe tratamiento o si un sano es vacunado.
    for individuo in oficina.individuos:
        try:
            distancia = random.randint(1, 3)
            direccion = random.randint(0, 2)
            posib = random.randint(0, 100)
            if direccion == DIR_IZQDA:
                print(individuo.id + " se desplaza "+str(distancia)+" a la izquierda.")
                individuo.desplazar(distancia, direccion)
            elif direccion == DIR_DCHA:
                print(individuo.id + " se desplaza "+str(distancia)+" a la derecha.")
                individuo.desplazar(distancia, direccion)
            # Además de los desplazamientos, vamos a incrementar en una semana el tiempo para los infectados
            if type(individuo).__name__ == "Infectado":
                for i in range(0,3): #En cada iteración de la simulación pasan 3 dias
                    individuo.incrementar_dia()

                # Vamos a decidir si el infectado recibe tratamiento (tiene un 5% de posibilidades)
                if not individuo.recibe_tratamiento and posib < POSIB_RECIBIR_TRATAMIENTO:
                    print(individuo.id + " recibe tratamiento.")
                    individuo.recibir_tratamiento()
            elif type(individuo).__name__ == "Sano":
                if not individuo.inmune and not individuo.tiene_anticuerpos and not individuo.vacunado and posib < POSIB_VACUNAR:
                    print(individuo.id +" es vacunado.")
                    individuo.ser_vacunado()

        except ValueError as e:
            print(e)

# Comienza flujo del programa
oficina = FactoriaOficina.crear_oficina("Raven", 15, 6)

while oficina.hay_posibilidad_infeccion():
    # Mostramos situación actual
    oficina.extender_infeccion()
    oficina.actualizar_sanos()
    print(oficina)
    realizar_acciones_simulacion(oficina)
    key = input("Presione una tecla ...")



