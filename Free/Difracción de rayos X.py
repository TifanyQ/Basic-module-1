import math
import statistics
from scipy.constants import hbar, m_e, pi
conversion_factor = 1.602177e-19                                        #eV

# Ingreso de datos (ángulos)
onda = float(input("Ingresa la longitud de onda (Angstrom): "))
lista = [float(input("Ingresa los 8 ángulos: ")) for _ in range(1, 9)]

# Cálculos intermedios
listadostheta = [x / 2 for x in lista]
listaseno = [math.sin(math.radians(x)) for x in listadostheta]
distinterplanar = [onda / (2 * x) for x in listaseno]
listaseno2 = [x**2 for x in listaseno]
listadiv = [x / listaseno2[0] for x in listaseno2]

#Resultados parciales
print("Ángulo (theta): {}".format(listadostheta))
print("Seno del ángulo: {}".format(listaseno))
print("Seno^2 del ángulo: {}".format(listaseno2))
print("División: {}".format(listadiv))
print("Distancia interplanar: {}".format(distinterplanar))

# Obtención de los sigma
listasumatoria = []

for n in range(1, 5):
    m = n * listadiv[1]
    if abs(round(m) - m) < 0.1:
        primernumero = n
        listasumatoria.extend([primernumero] + [round(primernumero * x) for x in listadiv[1:]])
        listadea = [math.sqrt((onda ** 2 * x) / (4 * y)) for x, y in zip(listasumatoria[0:8], listaseno2[0:8])]

#Resultados_finales
print("Los valores sigma son: {}".format(listasumatoria))
print("Constante de red: {}".format(listadea))

# Cálculo del promedio y desviación estándar
promedio = statistics.mean(listadea)
desviacion_estandar = statistics.stdev(listadea)
print("El valor promedio de a es: {}".format(promedio))
print("La desviación estándar es: {}".format(desviacion_estandar))

#Calculo de la Energia de Fermi (eV)

n = (12 / promedio ** 3)                                            #Densidad numérica (concentración de electrones)_ [cm^{-1}]

Ef = hbar ** 2 * (3 * pi ** 2) ** (2 / 3) * n ** (2 / 3) / (2 * m_e)
Efermi = Ef / conversion_factor * 10 ** 4                           #conversión de J a eV y de cm a m  [eV]

print("La densidad electrónica (cm^-1) es: {}".format(n))
print("La energía de Fermi (eV) es: {}".format(Efermi))
