
def tabla():
    numero = int(input('Ingresa un número entero entre 1 y 20: '))
    if 1 < numero < 20:
        file = open('tabla.txt', 'w')
        for n in range(1, 13):
            x = n * numero
            tabla_multi = '{} x {} = {} \n'.format(n, numero, x)
            print(tabla_multi)
            file.write(tabla_multi)
        file.close()
    else:
        print('Ingresa otro numero')

tabla()

