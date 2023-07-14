
def funcionDecoradora(funcion):
    def funcionInterna(*args, **kwargs):
        print('La cantidad de argumentos que tiene la función es {}'.format(len(args) + len(kwargs)))
        resultado = funcion(*args, **kwargs)
        print('La función decoradora terminó de ejecutarse correctamente')
        return resultado
    return funcionInterna

@funcionDecoradora
def suma(*args):
    final = 0
    for num in args:
        final += num
    return final

resultado = suma(12, 7, 5)
print('La suma final es {}'.format(resultado))