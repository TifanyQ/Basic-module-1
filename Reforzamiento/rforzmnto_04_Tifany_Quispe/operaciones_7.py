import random

lista=[]

def numero_aleatorio():
    while len(lista) < 10:
        numero1 = random.randint(0, 100)
        lista.append(numero1)

    return lista


