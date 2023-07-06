"Manejo de errores"

def operacion(x,y):
    try:
        resultado = x + y

    except TypeError:
        print("No se puede calcular")
    else:
        print("La suma es: {}".format(resultado))

operacion(4, "Hola soy pianista")
operacion(50, 100)