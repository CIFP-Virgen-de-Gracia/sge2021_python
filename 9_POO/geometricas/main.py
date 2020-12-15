from triangulo import *
from cubo import *
from cono import *
from cilindro import *

def getValorEntero(msg):
    correcto = False
    while not correcto:
        try:
            valor = int(input(msg))
            correcto = True
        except ValueError:
            print("El valor de "+msg+ " debe ser numérico entero")
    return valor

def menu():
    salir = False

    while not salir:
        print("Qué desea introducir:")
        print("1. Triángulo")
        print("2. Rectángulo")
        print("3. Circunferencia")
        print("4. Cubo")
        print("5. Cono")
        print("6. Cilindro")
        print("0. Salir")
        opcion = getValorEntero("Opcion: ")

        if opcion == 0:
            salir = True
        elif opcion == 1:
            figura = crearTriangulo()
        elif opcion == 2:
            figura = crearRectangulo()
        elif opcion == 3:
            figura = crearCircunferencia()
        elif opcion == 4:
            figura = crearCubo()
        elif opcion == 5:
            figura = crearCono()
        elif opcion == 6:
            figura = crearCilindro()
        else:
            print("Opción incorrecta.")

        if not salir:
            print(figura)
            print("Perímetro: {0}\nArea: {1}".format(figura.getPerimetro(), figura.getArea()))

def crearTriangulo():
    base = getValorEntero("Base: ")
    altura = getValorEntero("Altura: ")
    print("Introduce los dos lados que faltan: ")
    lado2 = getValorEntero("Lado2: ")
    lado3 = getValorEntero("Lado3: ")
    return Triangulo(base, altura, base, lado2, lado3)

def crearRectangulo():
    base = getValorEntero("Base: " )
    altura = getValorEntero("Altura: ")
    return Rectangulo(base, altura)

def crearCircunferencia():
    radio = getValorEntero("Radio: ")
    return Circunferencia(radio)

def crearCubo():
    lado = getValorEntero("Lado: ")
    return Cubo(lado)

def crearCono():
    radio = getValorEntero("Radio: ")
    generatriz = getValorEntero("Generatriz: ")
    return Cono(radio, generatriz)

def crearCilindro():
    radio = getValorEntero("Radio: ")
    altura = getValorEntero("Altura: ")
    return Cilindro(radio, altura)

menu()

