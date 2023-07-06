
#Valores sigma para cada estructura
sigmaBCC = [2,4,6,8,10,12,14,16,18,20]
sigmaFCC = [3,4,8,11,12,16,19,20]
sigmaDIAMANTE = [3,8,11,16,19]
#sigmaSIMPLE = []

#Indices de miller para cada estructura
millerFCC=[111,200,220,311,222,400,331,420]
millerBCC=[110,200,211,220,311,222,400,331,420]
#millerDIAMANTE=[]
#millerSIMPLE=[]

ndatos = int(input("Ingrese la cantidad de valores de sigma (min 3): "))

if ndatos>=3 and ndatos<10:
    valoressigma = [int(input("Ingresa los valores sigma: ")) for _ in range(1,ndatos+1)]

if valoressigma==sigmaFCC:
    estructura = "FCC"
    print("La estructura es {} y Los indices de miller para la estructura es:{}".format(estructura, millerFCC))
elif valoressigma == sigmaBCC:
    print("No se puede obtener la estructura ni los indices de miller")

