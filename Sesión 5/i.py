
nombre=input("Ingresa tu nombres y apellidos: ")

lista = nombre.split()
apellidos=lista[-2] + " " + lista[-1]

print("Tu apellido es {}".format(apellidos))

