"Reforzamineto01 - Tipos de datos"

"1. El valor de ‘¡HI TuNombre!’ imprimirlo por pantalla, el texto "
"debe ser un string y deberás guardarlo en una variable llamada mi_saludo. "
"Tu nombre debe estar en otra variable."

nombre="Tifany"
mi_saludo=str("¡Hi {}!".format(nombre))
print(mi_saludo)

"2. Crea una variable tipo int. Luego, multiplica por 10 y restarle 10. Debes hacer todo"
"esto en dos pasos. Finalmente mostrar el resultado por pantalla."

var1=int(input("Ingresa un número de tipo entero:"))
resultado=var1*10-10
print("El resultado de la suma es: {}".format(resultado))

"3. Crear una variable tipo string y poder luego sumarla con otra variable tipo int, para"
"esto convertir una de las variables. Mostrar la suma en pantalla."

var2=str(input("Ingresa el 1er número:"))
var3=int(input("Ingresa el 2do número:"))
suma=int(var2)+var3
print("El resultado de la suma es: {}".format(suma))

"4.Hallar el volumen de una esfera, cada dato requerido para hallar el volumen debe"
"estar en una variable. Mostrar el volumen por pantalla."

radio=int(input("Ingresa el valor del radio:"))
volumen=4/3*3.1416*radio**3
print("El volumen de la esfera es {}".format(volumen))

"5.Crear un programa que partiendo de un sueldo en una variable, sepamos si es par o"
"impar. Utilizar módulo y condicional."

numero = int(input("Ingresa el valor de tu sueldo de tipo entero:"))

if numero % 2 == 0:
    print("El sueldo es un número es par")
else:
    print("El sueldo es un número es impar")

"6. Calcular la media de 5 datos (floats), cada dato debe estar en una variable y la media"
"también. Mostrar el resultado en pantalla."

var_1=float((input("Ingresa el primer dato tipo float:")))
var_2=float((input("Ingresa el segundo dato tipo float:")))
var_3=float((input("Ingresa el tercer dato tipo float:")))
var_4=float((input("Ingresa el cuarto dato tipo float:")))
var_5=float((input("Ingresa el último dato tipo float:")))
media=(var_1+var_2+var_3+var_4+var_5)/5
print("La media de los 5 datos es:{}".format(media))

"7. De 3 números asignados (tú los propones) a 3 variables se pide hallar la suma de los"
"valores de los módulos con 3, 5, y 7 respectivamente, mostrar en pantalla el valor de la"
"suma."

var_7 =abs(-5)+3
var_8 =abs(-2)+5
var_9 =abs(-6)+7
sumavar=var_7+var_8+var_9
print("La suma total es {}".format(sumavar))

"8.Usando la condicional if imprimir por pantalla si una lista está vacía o no, probar con"
"una lista vacía y otra con una lista vacía."

numlista=int(input("Elige una lista (1 o 2):"))
if numlista==1:
    lista1=[5,7,13,47,"Martha"]
    long1 = len(lista1)
    print("La lista no está vacia, tiene {} elementos".format(long1))
if numlista == 2:
    lista2=[]
    long2 = len(lista2)
    print("La lista está vacia")

"9.Elevar al exponente de 4 un número que su valor estará asignado a una variable y luego"
"restar este mismo valor multiplicado por dos (usar pow). Mostrar el resultado en pantalla."

var4= int(input("Ingresa un número:"))
resultado2=pow(var4,4) - var4*2
print("El resultado de la suma es: {}".format(resultado2))

"10. Crear un diccionario con los siguientes key: nombre, carrera, edad y año de"
"nacimiento, mostrar en pantalla el valor de este diccionario."

diccionario={'Nombre':"Lucia",'Carrera':"Crisolo",'Edad':5,'Año de nacimiento':20/2/1999}
print(diccionario)

"11. Identificar que tipo de dato se obtiene al elevar un número a la exponente de 5 y"
"luego dividirlo por 10. Mostrar el resultado en pantalla."

var5=int(input("Ingresa un número:"))
tipo=pow(var5,5)/10
print("El resultado es {} y el tipo de dato es {}".format(tipo,type(tipo)))

