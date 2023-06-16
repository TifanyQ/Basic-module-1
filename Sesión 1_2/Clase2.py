
"Tipos fundamentales de datos"

"list - Secuencias mutables de valores"

"tuple - Secuencias inmutables de valores - No podrán ser editados"

"set - Elaborar conjuntos únicos - No pueden existir datos iguales"

"dic - Contenedores con clave para accede"

"Ejemplo:"

lista=[3,5,4,6,7,"Lorena"]
tupla=(5,6,8,9,12)
conjunto=set([1,3,5,7,1,5,"Bienvenidos"])
diccionario={'Nombre':"Lucia",'Apellido':"Crisolo",'Edad':5}

print(conjunto)

"Devolución de datos"

var_1 = "80"
var_2 = 3600
var_3 = 48.90
var_4= "500"

suma_string=var_1 + var_4
print("{}".format(suma_string))

"Conversión"
conversion=int(var_1)  #De string a entero

print(conversion)
print("El tipo de dato de mi variable es: {}".format(type(conversion)))

suma=conversion+var_2
print("La suma de int es:{}".format(suma))

"Suma de dos variables: int + float = float"
suma_2=var_2+var_3
print("La suma de var_2 + var_3 es: {}".format(suma_2))

"Concatenación se refiere a suma de solo string"
suma_conc=str(var_1)+str(var_2)
print(suma_conc)
