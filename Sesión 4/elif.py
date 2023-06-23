var1=int(input("Ingrese calificación 1: "))
var2=int(input("Ingrese calificación 2: "))

if (var1 + var2)/2 >= 16:
    print("Aprobado con honores")
elif 13 < (var1 + var2)/2 < 16:
    print("Aprobado")
else :
    print("Desaprobado")