nombre=input("Por favor ingrese su nombre:")
apellido=input("Ingrese su apellido:")
edad=input("Ingrese su edad:")

print("Bienvenid@ {nombre_usuario} {apellido_usuario} usted tiene {edad_usuario} años".format(nombre_usuario=nombre,apellido_usuario=apellido, edad_usuario=edad))

#Find

"Cadena de caracteres con Python"
"Buscar el índice de inicio de una sub cadena de string. .find(valor)"

cadena="Metodologías ágiles"

indice = cadena.find("ágiles")
print("El índice inicial de la subcadena es: {}".format(indice))