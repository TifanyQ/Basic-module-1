
file = open("main_file/example2.txt", "w")

file.write("Caracteristicas en Python\n")
file.write("Lenguaje multiplataforme\n")
file.write("Basado en POO\n")
file.write("pYtHoN ES UN lenguage vacano")

file = open("main_file/example2.txt", "r")

print("Contenido: {}".format(file.read()))
file.close()