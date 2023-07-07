
"9. "
class Persona:
    def __init__(self):
        self.nombre = None
        self.edad = None

    def ingresar_nombre(self):
        nombre = (input("Ingrese su nombre: "))
        self.nombre = nombre

    def ingresar_edad(self):
        edad = int(input("Ingrese su nombre: "))
        self.edad = edad

class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo):
        self.nombre = nombre
        self.edad = edad
        self.sueldo = 0

    def impuestos(self):
        impuesto = 0
        if self.sueldo > 4000:
            impuesto = self.sueldo * 10 / 100
        return impuesto

nombre = input("Ingrese el nombre: ")
edad = int(input("Ingrese la edad: "))
sueldo = float(input("Ingrese el sueldo: "))

empleado = Empleado(nombre, edad, sueldo)

print("Sueldo del empleado:", empleado.sueldo)

print("Impuesto a pagar:", empleado.impuestos())