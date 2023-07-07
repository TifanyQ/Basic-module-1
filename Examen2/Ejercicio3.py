def ingreso_datos():
    lista_incorrectos=[]
    while True:
        try:
            dato1 = float(input("Primer dato: "))
            dato2 = float(input("Segundo dato: "))
            return dato1, dato2
        except ValueError:
            print("Ingrese otro valor")
            lista_incorrectos.append(dato1)
            lista_incorrectos.append(dato2)

def division_cero(a,b):
    try:
        resultado = a / b
        return resultado
    except ZeroDivisionError:
        print("Error en la división entre cero")

def suma(lista_incorrectos):
    suma=0
    for x in lista_incorrectos:
        suma = suma + x
    return suma


dato1, dato2 = ingreso_datos()
resultado_division = division_cero(dato1, dato2)
#suma_incorrectos = suma(lista_incorrectos)

print("Resultado de la división:", resultado_division)
#print("Suma de datos incorrectos:", suma_incorrectos)