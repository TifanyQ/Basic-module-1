
def funcionDecoradora(funcionParametro):

    def funcionInterna(*args):
        print("Antes de la ejecución de la función a decorar")
        resutado=funcionParametro(*args)
        print("Después de la ejecución de la función a decorar")
        return resutado
    return  funcionInterna

@funcionDecoradora
def suma(a, b, c, d, e):
    return a + b + c + d + e

print(suma(10, 25, 10, 40, 30))

def saludar(name, lastname, age):
    print("Hola {} {}, usted tiene {} años.".format(name,lastname,age))

nombre = input("Ingrese su nombre por favor")
apellido = input("Ingrese su apellido por favor")
edad = input("Ingrese su edad por favor")

saludar(nombre, apellido, edad)