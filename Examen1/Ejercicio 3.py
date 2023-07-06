
"Teniendo presente el uso y concepto de diccionarios en Python, realizar un"
"programa con los siguientes requerimientos (4 ptos)"

nombre = input("Ingrese su nombre ")
apellido = input("Ingrese su apellido ")
edad = input("Ingrese su edad ")
dni = input("Ingrese su dni ")

diccionario = {'nombre': nombre, "apellido": apellido,
               "edad": edad, "dni": dni}

# Las segundas partes
valores = list(diccionario.values())
print("La lista es {}: ".format(valores))

profesion = input("Ingrese su profesion")
diccionario["profesion"] = profesion

print("La nueva lista con el dato de profesión es {}: ".format(diccionario))

del diccionario["dni"]

print("La nueva lista sin el dato de dni es {}: ".format(diccionario))
