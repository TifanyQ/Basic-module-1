
"Usando las propiedades de la cadena"

"Método string"

cadena = "Conexión a base de python"

cadena_2 = cadena.replace(cadena[0:6], "pppp")
print(cadena_2)

"Elimininando espacios en blanco"

cadena_3="Conexión a base de datos con Python"
cadena_4=cadena_3.rstrip()

print(cadena_4)

"Elimininando espacios en blanco de mi cadena (antes)"

cadena_5= "              Conexión a base de datos ...     "
cadena_6=cadena_5.lstrip()

print(cadena_6)