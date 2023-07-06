import math

class Circulo:
    def __init__(self):
        self.radio = None
    def area(self):
        self.area = math.pi * self.radio ** 2

    def perimetro(self):
        self.perimetro = 2 * math.pi * self.radio

    def pedir_radio(self):
        while True:
            try:
                radio = int(input("Ingrese un valor: "))
                self.radio = radio
                return radio
            except ValueError:
                print("Ingrese nuevo valor")

ejercicio = Circulo()
ejercicio.pedir_radio()
ejercicio.area()
ejercicio.perimetro()

print("El área es: {}".format(ejercicio.area))
print("El perímetro es: {}".format(ejercicio.perimetro))