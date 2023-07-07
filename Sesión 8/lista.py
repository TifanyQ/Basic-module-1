"""
Manejo de archivos
"""

tecnologiasBackend = ["Python", "Java", "NodeJS\n"]
tecnologiasFrontend = ["Angular", "React JS", "Boostrap"]

"""
Apertura de nuestro archivo:
    a+ : Permite escribir varias lineas en nuestro archivo
    a+ :Escribe nuevas lineas de texto sin sobreescribir el contenido del archivo
"""

file = open("main_file/example3.txt", "a+")

file.writelines(tecnologiasBackend)
file.writelines(tecnologiasFrontend)


file.close()