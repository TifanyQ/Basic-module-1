class Datos:

    def imprimir(self):
        self.imprimir = str(self.edad) + ' ' + self.valor

    def pedir_edad(self):
        edad = int(input("Ingrese edad: "))
        self.edad = edad

    def pedir_nombre(self):
        valor = str(input("Ingrese su nombre y apellido: "))
        self.valor = valor

    def diccionario(self):
        valor = str(input("Ingrese su nombre y apellido: "))
        edad = int(input("Ingrese edad: "))
        self.diccionario = {'Nombre y Apellido': valor, 'Edad': edad}

"Primera impresión"
#calculadora = Datos()
#calculadora.pedir_nombre()
#calculadora.pedir_edad()
#calculadora.imprimir()

#print(calculadora.imprimir)

"Segunda impresión"
calculadora = Datos()
calculadora.diccionario()
print(calculadora.diccionario)
