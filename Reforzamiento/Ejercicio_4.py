
"4. Invierte y muestra en consola tu lista de cursos."

lista =["física molecular", "electromagnetismo", "física del estado sólido", "álgebra lineal", "mecánica cuántica"]

lista.append("Metodología")
lista.append("Investigación")
lista.append("Semiconductores")
lista.append("Óptica")
lista.remove("electromagnetismo")
lista.remove("Semiconductores")

#Inversión de la lista de cursos
lista.reverse()
print("La lista actualizada es: {} ".format(lista))

