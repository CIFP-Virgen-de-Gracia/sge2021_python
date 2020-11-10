#!/usr/bin/env python
lista=['Hoy','va','a','ser','un','buen','día']
cadena = input("Cadena:")

if cadena in lista:
    print("La cadena %s está en la lista" % cadena)
else:
    print("La cadena no está en la lista")

print("La cadena %s aparece %d en la lista" % (cadena, lista.count(cadena)))

cadena2 = input("Cadena a reemplazar:")
apariciones = lista.count(cadena)
pos=0

for i in range(0,apariciones):
    pos = lista.index(cadena,pos)
    lista[pos]=cadena2

print(lista)