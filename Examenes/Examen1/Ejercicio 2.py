import random
"Python - Práctica 1"

numero1 = random.randint(0, 8)
"2.Usando el concepto y funciones de listas, realizar un programa con"
"las siguiente características (3 ptos):"

lista = []

numero1 = random.randint(0, 9)
numero2 = random.randint(0, 9)
numero3 = random.randint(0, 9)
numero4 = random.randint(0, 9)
numero5 = random.randint(0, 9)
numero6 = random.randint(0, 9)
numero7 = random.randint(0, 9)
numero8 = random.randint(0, 9)
numero9 = random.randint(0, 9)
numero10 = random.randint(0, 9)

lista = []

lista.append(numero1)
lista.append(numero2)
lista.append(numero3)
lista.append(numero4)
lista.append(numero5)
lista.append(numero6)
lista.append(numero7)
lista.append(numero8)
lista.append(numero9)
lista.append(numero10)

print(lista)

lista2 = []

for i in range(0, len(lista)):
    numerolista2 = lista[i] ** 2
    lista2.append(numerolista2)

print(lista2)

lista3 = []

for i in range(0, len(lista)):
    numerolista3 = lista[i] ** 3
    lista3.append(numerolista3)

print(lista3)

listasuma = []
for i in range(0, len(lista)):
    suma = lista2[i] + lista3[i]
    listasuma.append(suma)

print(listasuma)

listasuma.reverse()

print(listasuma)
print(listasuma)
