
"6. Devuelve la cantidad de veces que se repite un curso"
"(agregarla previamente a la lista) dentro de la lista."

lista =["física molecular", "electromagnetismo", "física del estado sólido", "álgebra lineal", "mecánica cuántica"]

lista.append("Metodología")
lista.append("Investigación")
lista.append("Semiconductores")
lista.append("Óptica")
lista.remove("electromagnetismo")
lista.remove("Semiconductores")
lista.reverse()
lista.append("Metodología")
lista.append("Investigación")

#Lista sin repetición de algún elemento

listasinrep=set(lista)

#Determinación de la cantidad de veces de un elemento de la lista

for i in listasinrep:
    repeticiones=lista.count(i)
    print("El curso {} se repite {} vez(ces).".format(i,repeticiones))
