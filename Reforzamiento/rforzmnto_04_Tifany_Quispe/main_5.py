
#import Ejercicio_5

def validar_nombre_usuario(nombre_usuario):
    if 7 <= len(nombre_usuario) <= 12:
        print('ok')
    else:
        print("El nombre de usuario debe ser alfanumérico.")
        return 'Vuelve a ingresar el nombre'

# Ejemplo de uso
nombre_usuario = input("Ingrese un nombre de usuario: ")
validar_nombre_usuario(nombre_usuario)
