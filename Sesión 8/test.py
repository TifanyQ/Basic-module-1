
titulo1 = "Tecnologías Backend"

tecnologiasBackend = ["\nPython", "\nJava", "NodeJS\n"]

file = open("main_file/example4.txt", "a+")

tecnologiasBackend[0]=titulo1

file.writelines(tecnologiasBackend)

file.close()