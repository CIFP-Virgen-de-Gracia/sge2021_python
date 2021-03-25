from Factorias.FactoriaPueblo import FactoriaPueblo
from Pueblo import Pueblo
from Humano import Humano
from Zombie import Zombie
import random

def cambiar_turno(turno):
    turno += 1
    turno %= 2
    return turno

def pedir_personaje(pueblo, faccion):
    valorCorrecto = False
    while not valorCorrecto:
        try:
            id = input("Id del personaje "+faccion+": ")
            personaje = pueblo.seleccionar_personaje(id, faccion)
            valorCorrecto = True
        except ValueError:
            print("Debe seleccionar un id válido")
    return personaje

def obtener_humano(pueblo):
    obtenido = False
    n_personajes = 0
    while not obtenido and n_personajes < len(pueblo.personajes):
        p = pueblo.personajes[n_personajes]
        if type(p).__name__ == "Humano" and p.vivo:
            obtenido = True
        n_personajes += 1
    return p

def elegir_opcion(pueblo):
    """Elegiremos las opciones que tiene el humano"""
    print("1. Correr izquierda")
    print("2. Correr derecha")
    print("3. Trotar izquierda")
    print("4. Trotar derecha")
    print("5. Caminar izquierda")
    print("6. Caminar derecha")
    print("7. Gritar")
    print("8. Atacar")
    # No vamos a considerar en la simulación que los humanos también persiguen porque no tiene
    # mucho sentido pero podrían hacerlo según la codificación
    valor_correcto = False
    while not valor_correcto:
        try:
            opcion = int(input("Opción: "))
            if opcion < 1 or opcion > 8:
                print("El valor introducido no es correcto")
            else:
                valor_correcto = True
        except ValueError:
            print("El valor introducido no es correcto")
    return opcion

def realizar_accion(opcion, humano):
    try:
        if opcion == 1:
            humano.correr("IZQDA")
        elif opcion == 2:
            humano.correr("DCHA")
        elif opcion == 3:
            humano.trotar("IZQDA")
        elif opcion == 4:
            humano.trotar("DCHA")
        elif opcion == 5:
            humano.caminar("IZQDA")
        elif opcion == 6:
            humano.caminar("DCHA")
        elif opcion == 7:
            humano.gritar()
        elif opcion == 8:
            zombie = pedir_personaje(pueblo, "Zombie")
            humano.atacar(zombie)
    except ValueError as e:
        print(e)

def simular_mordida(pueblo, zombie):
    """Obtiene si hay humanos en la misma posición y les muerde aleatoriamente"""
    try:
        personajes_misma_posicion = pueblo.get_personajes_posicion(zombie.pos_x, "Humano")
        if len(personajes_misma_posicion) > 0:
            # Mordemos
            for p in personajes_misma_posicion:
                index = pueblo.personajes.index(p) # Obtenemos el índice del personaje en la lista del pueblo
                print(zombie.id + " muerde a " + p.id)
                pueblo.personajes[index] = zombie.morder(p)
    except ValueError as e:
        print(e)

def simular_zombies(pueblo):
    """Acciones:
    - Comprobar si estamos en la misma posición que algún humano y en ese caso morder
    - Decidir aleatoriamente si corren, caminan, trotan
    - Decidir aleeatoriamente si persiguen a alguien o dejan de perseguir"""
    for personaje in pueblo.personajes:
        if type(personaje).__name__ == "Zombie":
            try:
                simular_mordida(pueblo, personaje)

                # Si no hemos mordido, vamos a decidir aleatoriamente si corren, caminan o trotan,
                # si persiguen a alguien o dejan de perseguir.
                # 0: corre dcha, 1: corre izqda, 2: camina dcha, 3: camina izqda
                # 4: trota derecha, 5: trota izqda, 6: persiguen, 7: dejan de perseguir.
                opcion = random.randint(0, 7)
                if opcion == 0: #corre dcha
                    print(personaje.id + " corre a la derecha.")
                    personaje.correr("DCHA")
                elif opcion == 1: #corre izqda
                    print(personaje.id + " corre a la izquierda.")
                    personaje.correr("IZQDA")
                elif opcion == 2: #caminar dcha
                    print(personaje.id + " camina a la derecha.")
                    personaje.caminar("DCHA")
                elif opcion == 3: #caminar izqda
                    print(personaje.id + " camina a la izquierda.")
                    personaje.caminar("IZQDA")
                elif opcion == 4: #trotar dcha
                    print(personaje.id + " trota a la derecha.")
                    personaje.trotar("DCHA")
                elif opcion == 5: #trotar izqda
                    print(personaje.id + " trota a la izquierda.")
                    personaje.trotar("IZQDA")
                elif opcion == 6: #perseguir
                    humano = obtener_humano(pueblo)
                    print(personaje.id +" persigue a "+humano.id)
                    personaje.perseguir(humano)
                elif opcion == 7: #dejar de perseguir
                    #Dejará de perseguir a todos los humanos que persiga
                    print(personaje.id + " deja de perseguir a todos los humanos.")
                    for p in pueblo.personajes:
                        if type(p).__name__ == "Humano":
                            personaje.dejar_de_perseguir(p)

            except ValueError as e:
                print(e)

# Comienza flujo del programa
pueblo = FactoriaPueblo.crear_pueblo("Puertollano", 10, 5)
turno = 0

# Mientras haya supervivientes jugamos
while pueblo.hay_supervivientes():
    # Mostramos situación actual
    pueblo.actualizar_estado()
    print(pueblo)
    print("TURNO " + str(turno))
    humano = pedir_personaje(pueblo, "Humano")
    opcion = elegir_opcion(pueblo)
    realizar_accion(opcion, humano)
    simular_zombies(pueblo)
    turno = cambiar_turno(turno)



