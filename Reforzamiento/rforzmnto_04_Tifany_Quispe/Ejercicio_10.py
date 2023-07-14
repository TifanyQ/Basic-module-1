
def datos():
    nombre = input('Ingresa el nombre: ')
    apellido = input('Ingresa el apellido: ')
    edad = int(input('Ingresa la edad: '))
    file = open('agenda.txt','a+')
    texto = '{}, {}, {} \n'.format(nombre, apellido, edad)
    file.write(texto)
    file.close()

datos()