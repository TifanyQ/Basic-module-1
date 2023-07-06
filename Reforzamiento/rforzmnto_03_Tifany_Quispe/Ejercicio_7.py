
class Persona:
    def __init__(self, nombre, edad, sueldo):
        self.nombre = nombre
        self.edad = int(edad)
        self.sueldo = float(sueldo)

    def eda(self):
        if self.edad >= 18:
            print("Es mayor de edad")

        else:
            print("No es mayor de edad")

    def bonificacion(self):
        self.total = 120 / 100 * self.sueldo
        print("Su sueldo mas bonificación es {} ".format(self.total))


persona1 = Persona("Ana", 75, 154)
persona2 = Persona("Pepe", 25, 54)

persona1.eda()
persona1.bonificacion()
persona2.eda()
persona2.bonificacion()
