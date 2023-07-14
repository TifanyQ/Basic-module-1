def registro():
    nombre = input('Ingresa nombre: ')
    nota1 = int(input('Ingresa nota1: '))
    nota2 = int(input('Ingresa nota2: '))
    promedio = (nota1 + nota2) / 2
    file = open('calificaciones.txt', 'a+')
    promedio_final = '{} tiene de promedio de {}\n'.format(nombre, promedio)
    file.write(promedio_final)
    file.close()

def aprobacion(nombre_input):
    encontrado = False
    file = open('calificaciones.txt','r')
    #print("{}".format(file.read()))
    for dato_nombre in file:
        datos = dato_nombre.strip().split()
        nombre = datos[0]
        promedio = float(datos[4])

        if nombre == nombre_input:
            encontrado = True
            if promedio >= 13:
                print('El alumno {} ha aprobado'.format(nombre))
            else:
                print('El alumno {} no ha aprobado'.format(nombre))
        if not encontrado:
            print('No se encontró al alumno {} en el registro.'.format(nombre))
    file.close()

#registro()

nombre_input = input('Ingresa nombre: ')
aprobacion(nombre_input)
