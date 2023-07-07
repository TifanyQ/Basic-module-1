"Manejo de archivos"

"""
    r: Abre el archivo en modo de lectura
"""


file = open("main_file/example.txt", "r")   #Buscó automaticamente el archivo y renombró la ubicación

""""
    read(): Nos permite leer el contenido de un archivo
"""

print("El contenido de nuestro archivo 'example.txt': {}".format(file.read()))

file.close()