def datos():
    nombre = input("Ingresa tu nombre: ")
    apellido = input("Ingresa tu apellido: ")
    return nombre, apellido

def seguro():
    tseguro = input("Indicar el tipo de seguro: ")
    return tseguro

def edad():
    edad = int(input("Ingresa tu edad: "))
    if edad >= 18:
        print("Es mayor de edad")
    else:
        print("Es menor de edad")
