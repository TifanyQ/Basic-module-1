
"7. Borra el primer ítem de la lista usando debidamente su índice."

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

lista.pop(0)

print("La lista actualizada es: {}".format(lista))