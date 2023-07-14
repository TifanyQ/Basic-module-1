"Decoradores en Python"
"Creación interna de la función decoradora"


def funcionA(funcionB):

    "Creación interna de la función decoradora"
    def funcionC():

        print("1. Antes de ejecutar la función a decorar\n")
        #Función que está pasando por parámetro en la función decoradora.
        funcionB()
        print("2. Después de ejecutar la función a decorar \n")

    return funcionC()

@funcionA
def saludar():
    return print("Hola pythonista")

print(saludar)