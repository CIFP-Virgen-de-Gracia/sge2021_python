elementos = [1, 5, -2]

# Completa el ejercicio aquí
def agregar_una_vez(lista, el):
    try:
        if el in lista:
            raise ValueError
        else:
            lista.append(el)
    except ValueError:
        print("Error: Imposible añadir elementos duplicados =>", el)

agregar_una_vez(elementos, 10)
agregar_una_vez(elementos, -2)
agregar_una_vez(elementos, "Hola")

print(elementos)