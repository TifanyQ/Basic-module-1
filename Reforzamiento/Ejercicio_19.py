
"19. Crea una lista vacía (con 10 posiciones), pide sus"
"valores y devuelve la suma y la media de los números."

lista=[]

#Realizar lista por ingreso de elementos
while len(lista)<10:
    num = input("Ingresa el número: ")
    lista.append(num)
print(lista)

#Suma de todos los elementos de la lista
suma=int(0)
for i in range (0,len(lista)):
    suma=suma+int(lista[i])
print("La suma de todos los elementos es {}".format(suma))