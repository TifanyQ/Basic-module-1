"Lissta4"
"del"

lista=[5,78,6,15,46,32,48]

del lista[2]

print(lista)

for i in range(len(lista)):
    print("La posición en {} es {}".format(i,lista[i]))
print(lista)

"Diccionarios"

diccionario={"nombre":"python","key":"Java"}
print(diccionario)

diccionario["antiiguedad"]=14
diccionario["administrativa"]="a,b,c"
print(diccionario)

del diccionario["nombre"]
print(diccionario)

keys = sorted(diccionario)  #Las primeras partes de dos
print(keys)

valores=list(diccionario.values())
print(valores)

hola2=list(diccionario.keys()) #Las segundas partes
print(hola2)

"Convirtiendo el diccionario en una lista"

lista_convertida=diccionario.items()
print(lista_convertida)

