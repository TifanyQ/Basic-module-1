from scipy.constants import hbar, m_e, pi
conversion_factor = 1.602177e-19  #eV
a=4.04951e-10
#Energía de Fermi
Ef = hbar**2*(3*pi**2)**(2/3)*12**(2/3)/(2*m_e*a**2)
Efermi=Ef/conversion_factor
print(Ef)
print(Efermi)

