
"17. Crear una lista con los 10 primeros números al cuadrado y "
"mostrar el resultado en terminal."

lista=[]

for i in range (1,11):
    numero=i**2
    lista.append(numero)

print("El cuadrado de los 10 primeros números es {}".format(lista))