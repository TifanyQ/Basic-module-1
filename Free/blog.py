from scipy.constants import hbar, m_e, pi, e
import math

conversion_factor = 1.602177e-19                                        #eV

"Cálculo de la Energia de Fermi"
#Parámetro de red
a=4.04951e-8                                                            #cm

#Densidad numérica (concentración de electrones)
n = (12 / a ** 3)                                                      #[cm^{-1}]
#Energía_Fermi (eV)
Ef = hbar ** 2 * (3 * pi ** 2) ** (2/3) * n ** (2/3)/(2 * m_e)
Efermi = Ef * 10 ** 4 / conversion_factor                   #conversión de J a eV y de cm a m  [eV]

print("La densidad electrónica (cm^-1) es: {}".format(n))
print("La energía de Fermi (eV) es: {}".format(Efermi))

k_feri = (n * 3 * pi ** 2) ** (1/3)
v = math.sqrt(Efermi*2*m_e/(10**4)) / (m_e)
l = 2 * 10**(-6)

print("Velocidad de Fermi es: {}".format(v))

"Conductividad"
res = v * m_e / (e ** 2 * n * l)

print(res)
