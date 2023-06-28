"Usando las propiedades de cadenas"

"Métodos STRING"

mi_cadena="Machine Learning"

"Convirtiendo a mayúscula mi cadena"

print("Conversión: {}".format(mi_cadena.upper()))

mi_cadena2="Machine Learning"

"Convirtiendo a minúscula"

print("Conversión minúscula:{}".format(mi_cadena.lower()))

"Convirtiendo a un tipo title"

print("{}".format(mi_cadena2.title()))

#Ejercicio......................................................

nombre= input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")

print("Bienvenido {} {}!!".format(nombre,apellido))

concatenacion=nombre + " " + apellido

print("El tamaño es: {}".format(len(concatenacion)))
print("{}".format(concatenacion.upper()))

if len(nombre) > len(apellido):
    print("El tamaño del nombre es mayor que del apellido")
else:
    print("El tamaño del nombre es menor que del apellido")

