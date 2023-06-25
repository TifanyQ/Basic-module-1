
"5. Obtén la cantidad total ítems que tienes en tu lista creada y mostrar el resultado en"
"consola. (Pista: len(lista))"

lista =["física molecular", "electromagnetismo", "física del estado sólido", "álgebra lineal", "mecánica cuántica"]

lista.append("Metodología")
lista.append("Investigación")
lista.append("Semiconductores")
lista.append("Óptica")
lista.remove("electromagnetismo")
lista.remove("Semiconductores")
lista.reverse()

print("La cantidad total de item de la lista actualizada es: {} ".format(len(lista)))


