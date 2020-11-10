#!/usr/bin/env python
def crearLista():
    numero = int(input("Número de palabras de la lista:"))

    if numero < 1:
        print("Error. Debe ser un número >= 1")
        return -1
    else:
        lista = []
        for i in range(numero):
            print("Palabra ", str(i + 1) + ": ", end="")
            palabra = input()
            lista.append(palabra)
        return lista

def eliminarRepetidos(lista):
    #Vamos a eliminar los elementos repetidos
    for i in range(len(lista)-1,-1,-1): #La recorremos de forma inversa porque eliminamos repetidos
        if lista[i] in lista[:i]:
            del(lista[i])
    return lista

def elementosComunes(lista1, lista2):
    comunes = []
    for i in lista1:
        if i in lista2:
            comunes.append(i)
    return comunes

def elementosSoloUnaLista(lista1,lista2):
    elementos = []
    for i in lista1:
        if i not in lista2:
            elementos.append(i)
    return elementos

primera = crearLista()
primera = eliminarRepetidos(primera)
print("Primera lista sin repetidos: ", primera)
segunda = crearLista()
segunda = eliminarRepetidos(segunda)
print("Segunda lista sin repetidos: ", segunda)
comunes = elementosComunes(primera,segunda)
print("Palabras que aparecen en las dos listas: ", comunes)
elementosSoloPrimera = elementosSoloUnaLista(primera, segunda)
print("Palabras que aparecen sólo en la primera: ", primera)
elementosSoloSegunda = elementosSoloUnaLista(segunda, primera)
print("Palabras que aparecen sólo en la segunda: ", segunda)


