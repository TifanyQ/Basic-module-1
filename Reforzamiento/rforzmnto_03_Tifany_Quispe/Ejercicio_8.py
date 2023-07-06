
class Agenda:
    def __init__(self):
        self.lista = []

    def agregar_contacto(self, nombre, telefono, email, dni):
        contacto = {
            'nombre': nombre,
            'telefono': telefono,
            'email': email,
            'dni': dni
        }
        self.lista.append(contacto)

    def mostrar_contacto(self):
         for contacto in self.lista:
            print("Nombre:".format(contacto['nombre']))
            print("Teléfono: {}".format(contacto['telefono']))
            print("Email: {}".format(contacto['email']))
            print("DNI: {}".format(contacto['dni']))

    def buscar_contacto_por_dni(self, dni):
        for contacto in self.lista:
            print("DATOS")
            print("Nombre: {}".format(contacto['nombre']))
            print("Teléfono: {}".format(contacto['telefono']))
            print("Email: {}".format(contacto['email']))
            print("DNI: {}".format(contacto['dni']))
            return

agenda = Agenda()

agenda.agregar_contacto("Ana Lucia", "935214687", "lucia@gmail.com", "32025963")
agenda.agregar_contacto("Ana Laura", "936587254", "laura@gmail.com", "3845682")

agenda.buscar_contacto_por_dni("32025963")
agenda.buscar_contacto_por_dni("3845682")
