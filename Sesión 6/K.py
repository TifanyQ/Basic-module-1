"""
    Programación orientada a objetos
"""
class Carro:                #Primera letra en mayúscula
    "Atributos"
    ruedas = 4

    "Constructor: Valores que van a tener por defecto mi clase cuando se le instancia a una variable"
    def __init__(self, color_1, aceleracion_1):
        self.color = color_1
        self.aceleracion = aceleracion_1
        self.velocidad = 0

    "Métodos: Son las funciones de la clase"
    def acelerar(self):
        self.velocidad = self.velocidad + self.aceleracion

    def frena(self):
        velocidad = self.velocidad - self.aceleracion
        if velocidad <0:
            velocidad = 0
        self.velocidad = velocidad

"Instanciamos nuestra clase"
print("Carro_1")
carro_1 = Carro("negro",50)
print("Color: {}".format(carro_1.color))
print("Acelertación: {}".format(carro_1.aceleracion))
print("Ruedas:{}".format(carro_1.ruedas))

print("Carro_2")
carro_2=Carro("azul",70)
print("Color: {}".format(carro_2.color))
print("Acelertación: {}".format(carro_2.aceleracion))
print("Ruedas:{}".format(carro_2.ruedas))

carro_1=Carro("Blanco", 30)

print("El color es: {}".format(carro_1.color))


class Carrovolador:

    ruedas = 6

    def __init__(self, color, aceleracion, estado_volando=False):
        super().__init__(color,aceleracion)
        self.estadovolando = estado_volando

    def vuela(self):
        self.estadovolando = True

    def aterriza(self):
        self.estadovolando = False

#carro_3 = Carro("Rojo", 70)

carro_volador = Carrovolador("Blanco", 50)
print("El estado inicial es: {}".format(carro_volador.estadovolando))