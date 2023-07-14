def funcionDecoradora(funcion):
    def funcionInterna(*args):
        print('Buenos dias')
        resultado = funcion(*args)
        print('Hasta luego')
        return resultado
    return funcionInterna


@funcionDecoradora
def nombre():
    nombre_input = input('Ingrese nombre: ')
    mensaje = 'Soy {}'.format(nombre_input)
    return mensaje

mensaje = nombre()
print(mensaje)
