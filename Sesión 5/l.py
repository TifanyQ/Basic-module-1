
var_1=float(input("Ingresa el primer valor: "))
var_2=float(input("Ingresa el segundo valor: "))
var_3=float(input("Ingresa el tercer valor: "))

def media(x,y,z):
    promedio=(x+y+z)/3
    return promedio

suma=media(var_1,var_2,var_3)

print("La media de los 3 valores es: {}".format(suma))