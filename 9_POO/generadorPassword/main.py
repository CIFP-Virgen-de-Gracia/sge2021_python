from password import Password


def numPassword():
    valorcorrecto = False
    npassword = 0
    while not valorcorrecto:
        try:
            npassword = input("Introduce el número de password que deseas generar: ")
            npassword = int(npassword)
            valorcorrecto = True
        except ValueError:
            print("La longitud debe ser un entero")
    return npassword


def generarListaPassword():
    npassword = numPassword()

    listapassword = []
    long = -1
    for i in range(npassword):
        msg = "Longitud de la contraseña {0} (-1 para longitud por defecto): "
        valorcorrecto = False
        while not valorcorrecto:
            long = input(msg.format(str(i)))
            try:
                long = int(long)
                valorcorrecto = True
            except ValueError:
                print("La longitud debe ser un entero")
        if long == -1:
            listapassword.append(Password())
        else:
            listapassword.append(Password(long))
    return listapassword


def mostrarListaPassword(listapassword):
    for p in listapassword:
        print(p)


# Creamos la lista de contraseñas y la mostramos por pantalla
listapassword = generarListaPassword()
mostrarListaPassword(listapassword)
