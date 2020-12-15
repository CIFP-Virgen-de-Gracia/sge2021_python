#!/usr/bin/env python
isNumber = False
while not isNumber:
	try:
		x = int(input("Introduce un número:"))
		isNumber = True
	except ValueError:
		print ("Debes introducir un número")

print(x)