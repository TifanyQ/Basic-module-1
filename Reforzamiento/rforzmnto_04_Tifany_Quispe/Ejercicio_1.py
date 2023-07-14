

def suma(x, y):
    try:
        res = x + y
    except TypeError:
        print('No se puede calcular')
        print('Ingresa nuevo valores')

    else:
        print(res)

suma(80, 'k')