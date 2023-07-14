import operaciones_8
import math

numero1 = operaciones_8.ingreso_valor()
def raiz_cuadrada():
    raiz = math.sqrt(numero1)
    print('La raiz del número es: {}'.format(raiz))
def cuadrado_cubo():
    cuadrado = numero1**2
    cubo = numero1 **3
    print('El cuadrado es {} y el cubo es {}'.format(cuadrado, cubo))

raiz_cuadrada()
cuadrado_cubo()


