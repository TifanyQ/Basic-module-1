
"Modelo de Drude_Conductividad"

from scipy.constants import hbar, m_e, N_A, e, eV

"Datos de ingreso"

tao = input()
campo_electrico = input()
cant_e =
valencia =

"Cálculos intermedios"

vol = a**3  #Parámetro de red

#Densidad numérica electrónica
n = cant_e * valencia * N_A / vol

#fuerza_electrica= e*campo_electrico = masa*velocidad/tao

mu = e * tao / m_e  #movilidad

velocidad = campo_electrico * mu

#conductividad = n * e^2 * tao / m

conductividad = n * e * mu
resistividad = 1 / conductividad

#densidad_corriente = densidad (n) * e * velocidad = n * e^2 * tao / m * campo_electrico=
#densidad_corriente = conductividad * campo_electrico

densidad_corriente = conductividad * campo_electrico

print(m_e)