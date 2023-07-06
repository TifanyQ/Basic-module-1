class Calculo:
    def __init__(self):
        self.valor = None

    def cuadrado(self):
        self.cuadrado = self.valor ** 2

    def cubo(self):
        cubo = self.valor ** 3
        self.cubo = cubo

    def pedir_valor(self):
        valor = int(input("Ingrese un valor: "))
        self.valor = valor

calculadora = Calculo()
calculadora.pedir_valor()
calculadora.cubo()
print(calculadora.cubo)
