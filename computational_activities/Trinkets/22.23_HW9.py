# Import Libraries
import scipy.constants as sp
import math

# Variables

n1_turns = 4600
n2_turns = 2600
radius_c1 = 0.04
radius_c2 = 0.02
distance = 0.4
current = 0.05
freq = 2100

# Calculations

mu0_4pi = sp.mu_0/(4*sp.pi)
area_c1 = math.pow(radius_c1,2) * sp.pi
area_c2 = math.pow(radius_c2,2) * sp.pi
ang_freq = freq * 2 * sp.pi
l_third = 1/math.pow(distance,3)
emf_c2 = n1_turns * n2_turns * mu0_4pi * 2 * area_c1 * area_c2 * current * ang_freq * l_third

# Print
print("The maximum voltage of the second coil voltage =", emf_c2,"V")
