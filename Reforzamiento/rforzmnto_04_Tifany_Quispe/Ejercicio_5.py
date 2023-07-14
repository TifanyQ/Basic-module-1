def validar_nombre_usuario(nombre_usuario):
    if nombre_usuario.isalnum():
        print("El nombre de usuario es válido.")
    else:
        print("El nombre de usuario debe ser alfanumérico.")


# Ejemplo de uso
nombre_usuario = input("Ingrese un nombre de usuario: ")
validar_nombre_usuario(nombre_usuario)
