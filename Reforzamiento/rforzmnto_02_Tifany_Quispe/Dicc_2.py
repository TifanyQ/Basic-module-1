
#Conversión de diccionario a lista
diccionario={'Nombre':"Lucia",'Edad':8,'Salario':15875}

lista=list(diccionario.keys())+list(diccionario.values())

print("La lista actualizada: {}".format(lista))
print("El tipo de datos es: {}".format(type(lista)))