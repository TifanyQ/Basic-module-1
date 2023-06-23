var1=int(input("Ingrese calificación parcial: "))
var2=int(input("Ingrese calificación final: "))

if (var1 + var2)/2 >= 16 and var3 >> 15:
    print("Aprobado con honores")
elif 13 < (var1 + var2)/2 < 16:
    print("Aprobado")
else :
    print("Desaprobado")
    var3=int(input("Ingrese calificación sustitutorio: "))
    if var3 > var1 or var2:
        var4 = (var1+var2)/2
        promedio=(var3 + var4)/2
        print("Su nueva calificación es {}".format(promedio))


