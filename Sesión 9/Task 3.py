

# Previo al uso de conocimiento de los **kwargs
#print("Hola {nombre} usted tiene {edad} años".format(edad='35', nombre='Lorena'))

def paciente(nombre, ciudad, fecha):
        return "El paciente '{}' es de {} y le dieron de alta: {}".format(nombre, ciudad, fecha)

#print(paciente("Karina", "Lima", "06 de julio del 2023"))

"Uso del **kargs"

def paciente(**kwargs):
    saludo = "El paciente {} es de {} y le dieron de alta: {}"
    i = 0
    for key, value in kwargs.items():
        if i==0:
            print(key)
            print(value)
            saludo = 'El paciente {}'.format(value)
        elif i == 1:
            saludo = saludo + " es de {}".format(value)
        else:
            saludo = saludo + " y le dieron de alta el: {}".format(value)
        i = i + 1

    return saludo
        #"Saludo finalizado"

print(paciente(nombre="Karina", ciudad="Lima", fecha="6 de julio"))