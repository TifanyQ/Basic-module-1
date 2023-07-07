import datetime

class Persona:
    def __init__(self):
        self.nombre = None
        self.apellido = None

    def pedir_nombre(self):
        nombre = input("Ingrese nombre: ")
        self.nombre = nombre

    def pedir_edad(self):
        while True:
            try:
                edad = int(input("Ingrese edad: "))
                self.edad = edad
                return edad
            except ValueError:
                print("Ingrese nuevo valor")

    def metodo(self):
        self.metod = self.edad + 1
        print("Edad: {}".format(self.metod))
        return

persona1 = Persona()
persona1.pedir_nombre()
persona1.pedir_edad()
persona1.metodo()
persona1.metodo()

print(persona1.pedir_edad)


