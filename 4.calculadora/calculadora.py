#!/usr/bin/env python

salir = False
operandos = False
while not salir:
    operacion = input("Introduzca una operación válida: +, -, *, /, ^ (-1 para salir)")
    if (operacion != '+' and operacion != '-' and operacion != '*' and operacion != '/' and operacion != '^' and operacion != '-1'):
        print("Error, la operación no es válida")
    elif operacion == '-1':
        salir = True
    else:
        while not operandos:
            operando1 = float(input("Introduzca un operando:"))
            operando2 = float(input("Introduzca el segundo operando:"))
            if((type(operando1) != int and type(operando1) != float) or (type(operando2) != int and type(operando2) != float)):
                print("Error, los operandos deben ser numéricos")
            else:
                operandos = True
                operando1 = float(operando1)
                operando2 = float(operando2)
                if operacion == '+': print("El resultado de %.2f %s %.2f es %.2f" % (operando1, operacion, operando2, float(operando1+operando2)))
                elif operacion == '-': print("El resultado de %.2f %s %.2f es %.2f" % (operando1, operacion, operando2, float(operando1-operando2)))
                elif operacion == '*': print("El resultado de %.2f %s %.2f es %.2f" % (operando1, operacion, operando2, float(operando1*operando2)))
                elif operacion == '/': print("El resultado de %.2f %s %.2f es %.2f" % (operando1, operacion, operando2, float(operando1/operando2)))
                elif operacion == '^': print("El resultado de %.2f %s %.2f es %.2f" % (operando1, operacion, operando2, float(operando1**operando2)))
