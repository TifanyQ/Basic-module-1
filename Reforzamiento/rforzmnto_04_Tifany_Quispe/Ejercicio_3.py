def persona(x):
    try:
        persona_lista = {'nombre': 'Xavier', 'apellido': 'Rodriguez', 'dni': '63325345'}
        res = persona_lista[x]

    except KeyError:
        print('El key ({}) no se encuentra registrado en el diccionario'.format(x))

    else:
        print(res)

persona('profesion')