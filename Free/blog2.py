try:
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))

    resultado = num1 / num2

    print("El resultado de la división es:", resultado)

except ZeroDivisionError:
    print("Error: No se puede dividir entre cero.")

except ValueError:
    print("Error: Ingrese solamente números enteros.")

