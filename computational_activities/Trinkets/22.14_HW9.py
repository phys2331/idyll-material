# Import Libraries
import scipy.constants as sp
import math

# Variables

r_sol = 0.05
r_wire = 0.11
l_sol = 3
N_sol = 9000
I_rate = 41

# Calculations

area_sol = sp.pi * r_sol**2
B_sol = (sp.mu_0 * N_sol * I_rate)/l_sol
emf = (B_sol * area_sol)
E_NC = emf/(2 * sp.pi * r_wire)

# Print

print("Part 1: The average emf in the wire =", emf, "V")
print("Part 2: The non-Coulomb electric field in the wire =", E_NC, "V/m")
