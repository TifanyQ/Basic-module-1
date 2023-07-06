def funcion(dato1, dato2):
    if dato2 > dato1:
        for x in range(dato1 + 1, dato2):
            cuadrado = x ** 2
            print(cuadrado)

numero1 = int(input("Por facor, ingrese el primer número: "))
numero2 = int(input("Por favor,ingrese el segundo número: "))
funcion(numero1, numero2)
