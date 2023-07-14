
def item(i):
    try:
        lista_base=[2,6,10,4,5,23,1]
        res = lista_base[i]

    except IndexError:
        print('Valor fuera de rango')

    else:
        print(res)

item(10)