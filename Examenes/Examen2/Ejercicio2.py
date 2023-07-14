import datetime

class Persona:
    def __init__(self, nombre, saldo):
        self.nombre = nombre
        self.saldo = saldo

    def mostrar_saldo(self):
        print("Su saldo es: {}".format(self.saldo))

    def transferencia(self,transfer):
        self.transfer = transfer
        if self.saldo > self.transfer:
            self.transferencia = transfer
            print("Estimado(a) {}, se realizará la transferencia".format(self.nombre))
        else:
            print("Estimado(a) {}, no tiene el dinero suficiente para realizar la transferencia".format(self.nombre))

persona1 = Persona("Ana", 50)
persona1.mostrar_saldo()
trans1 = persona1.transferencia(10)

persona2 = Persona("Jose", 20)
persona2.mostrar_saldo()
trans2 = persona2.transferencia(30)
