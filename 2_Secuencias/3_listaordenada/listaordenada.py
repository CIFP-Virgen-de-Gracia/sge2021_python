#!/usr/bin/env python
lista=[2,3,4,1]
lista2=lista[:] #Copia
lista.sort()
if lista == lista2:
    print("Lista ordenada")
else:
    print("Lista no ordenada")