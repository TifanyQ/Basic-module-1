"Python - Práctica 1"
"1. Usando los tipos de datos y sus conversiones "
"realizar lo siguiente. (3 ptos)"

print("Ingresa los datos del primer trabajador")
nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))

print("Buenas noches {} con {} años.".format(nombre, edad))
print("El nombre es de tipo {} y la edad es tipo {}"
      .format(type(nombre), type(edad)))

print("Ingresa los datos del segundo trabajador")
nombre2 = input("Ingrese su nombre: ")
edad2 = int(input("Ingrese su edad: "))

print("Buenas noches {} con {} años.".format(nombre2, edad2))

lista = [nombre, edad]
lista2 = [nombre2, edad2]

suma = lista[1] + lista2[1]

print("La suma de las edades de ambos trabajadores es : {}".format(suma))
