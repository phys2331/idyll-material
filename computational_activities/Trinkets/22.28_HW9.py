# Import Libraries
import scipy.constants as sp
import math

# Variables
height = 67
length = 20
current = 3E4
freq = 60
h_body = 2
w_body = 0.5

# Calculations
r = math.sqrt(height**2 + ((length**2)/4))
sin_theta = length/(2*r)
ang_freq = 2 * sp.pi * freq
area_body = h_body * w_body
B = (((sp.mu_0*current)/(2*sp.pi*r))*2)*sin_theta
max_emf = B * area_body * ang_freq
max_emf_mV = max_emf * 1000

# Print

print("Part 1: The magnitude of the magnetic field =", B, "T")
print("Part 2: The maximum emf =", max_emf_mV, "mV")
