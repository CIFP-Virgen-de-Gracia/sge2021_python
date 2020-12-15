def agregarAlumno(almacenAlumnos, nombre, apellidos, dni):
    alumno = {"nombre": nombre, "apellidos": apellidos }
    """Si el dni existía en el almacén será sobreescrito"""
    almacenAlumnos[dni]=alumno

def mostrarAlumnos(almacenAlumnos):
    for dni,alumno in almacenAlumnos.items():
        print("DNI:", dni, alumno)

def buscarAlumnos(almacenAlumnos, **kwargs):
    resultadosBusqueda = [];
    if "dni" in kwargs.keys():
        alumno = almacenAlumnos[dni];
        resultadosBusqueda.append(alumno);
    else:
        almacenFiltrado = almacenAlumnos.values();
        alumnoBuscado = True
        for alumno in almacenFiltrado:
            for name,value in kwargs.items():
                if alumnoBuscado and alumno[name] != value: alumnoBuscado = False
            if alumnoBuscado: resultadosBusqueda.append(alumno)
            else: alumnoBuscado = True

    return resultadosBusqueda;

if __name__ == '__main__':
    almacenAlumnos = {}
    parar = False
    nombre = ""
    apellidos = ""
    dni = ""
    while not parar:
        print("Introduzca los datos del alumno (S para salir)")
        nombre = input("Nombre: ")
        if(nombre != "S"):
            apellidos = input("Apellidos: ")
            if (apellidos != "S"):
                dni = input("DNI: ")
            else: parar = True
        else: parar = True
        if (not parar):
            agregarAlumno(almacenAlumnos, nombre, apellidos, dni)

    print(buscarAlumnos(almacenAlumnos, nombre="Inma", apellidos="Gijón"))