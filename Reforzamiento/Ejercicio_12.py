
"12. Reconocer los tipos de cada dato en la lista creadas y mostrarla en consola (type())"

lista=[57.3,False,98.1,12.7,True,34.1,False,98.4]

for i in range(len(lista)):
    print("El item {} con valor {}, es de tipo {}".format(i,lista[i],type(lista[i])))

