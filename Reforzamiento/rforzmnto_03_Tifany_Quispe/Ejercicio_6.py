
class Alumno:
    def __init__(self, nombre, edad,notafinal):
        self.nombre = nombre
        self.edad = edad
        self.notafinal = notafinal

    def datos(self):
        print("Nombre: ", self.nombre)
        print("Edad: ", self.edad)
        print("Nota Final: ", self.notafinal)
    def notafi(self):
        if self.notafinal >= 11:
            print("Ha aprobado")
        else:
            print("Ha desaprobado")

nombre1 = Alumno("Carlos",15,16)
nombre2 = Alumno("Alejandro",18,8)
nombre3 = Alumno("Maria",22,12)

nombre1.datos()
nombre1.notafi()

nombre2.datos()
nombre2.notafi()