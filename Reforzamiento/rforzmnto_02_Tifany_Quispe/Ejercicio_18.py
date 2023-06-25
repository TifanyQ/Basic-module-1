
"18. Crear una lista con los 15 primeros números impares, luego agregar 3 números flotantes"
"repetidos (los cuales son impares dentro del rango indicado y que no sea el último impar)."
"- Empezando desde 1 y no 0."
"- Agregar un cadena en la posición 3 de la lista."
"- Eliminar este valor string de la cadena usando del."

lista=[]
lista.append(1)
num=1

while len(lista) < 15:
    num=num+2
    lista.append(num)

#Agregado de 3 números flotantes repetidos impares
lista.append(float(7))
lista.append(float(7))
lista.append(float(7))

#Agregado de una cadena en la posición 3 de la lista actualizada
lista.insert(3,str("25"))

#Eliminado del string creado usando del
del lista[3]

print("La lista actualizada es: {}".format(lista))
