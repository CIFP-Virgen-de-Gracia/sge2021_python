#!/usr/bin/env python

# La primera letra de cada palabra. Por ejemplo, si recibe Universal Serial Bus debe devolver USB.
def iniciales(cadena):
    lista=cadena.split(" ")
    iniciales=""
    for palabra in lista:
        iniciales += palabra[0]
    return iniciales

# Dicha cadena con la primera letra de cada palabra en mayúsculas. Por ejemplo, si recibe república argentina debe devolver República Argentina.
def capitalizacion(cadena):
    lista = cadena.split(" ")
    capitalizadas = ""
    for palabra in lista:
        capitalizadas += palabra.capitalize() + " "
    return capitalizadas

# Las palabras que comiencen con la letra A. Por ejemplo, si recibe Antes de ayer debe devolver Antes ayer.
def palabrasComiencenA(cadena):
    lista = cadena.split(" ")
    resultado = ""
    for palabra in lista:
        if palabra.startswith("a") or palabra.startswith("A"):
            resultado += palabra + " "
    return resultado

cad=input("Cadena:")
print(iniciales(cad))
print(capitalizacion(cad))
print(palabrasComiencenA(cad))
