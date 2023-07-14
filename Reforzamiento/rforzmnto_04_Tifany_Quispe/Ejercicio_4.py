def div(x):
    try:
        division = x / 0

    except TypeError:
        print('División de un string entre cero no se puede efectuar')

    else:
        print(division)

string = 'Hellos Pythonista'
div(string)

