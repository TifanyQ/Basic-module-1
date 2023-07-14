def funcionDecoradora(funcion):
    def funcionInterna(*args, **kwargs):
        print('Está por ejecutarse la función')
        resultado = funcion(*args, **kwargs)
        print('La función ha sido ejecutado correctamente')
        return resultado
    return funcionInterna

@funcionDecoradora
def producto(*args, **kwargs):
    resultado = 1
    for arg in args:
        resultado *= arg
    for key, value in kwargs.items():
        resultado *= value
    return resultado

resultado = producto(2, 3, 14, 5)
print(resultado)