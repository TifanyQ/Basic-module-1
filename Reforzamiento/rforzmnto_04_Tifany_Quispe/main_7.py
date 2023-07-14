import operaciones_7

def orden_numeros():
    numeros=operaciones_7.numero_aleatorio()
    numeros.sort()
    return numeros

lista_actualizada=orden_numeros()
print(lista_actualizada)