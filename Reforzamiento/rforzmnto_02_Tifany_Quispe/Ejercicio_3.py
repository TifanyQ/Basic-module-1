
"3. Quita 2 elementos de tu nueva lista ítems por valor, no por índice."

lista =["física molecular", "electromagnetismo", "física del estado sólido", "álgebra lineal", "mecánica cuántica"]

lista.append("Metodología")
lista.append("Investigación")
lista.append("Semiconductores")
lista.append("Óptica")

#Eliminado de dos elementos
lista.remove("electromagnetismo")
lista.remove("Semiconductores")

print("La lista actualizada es: {} ".format(lista))


