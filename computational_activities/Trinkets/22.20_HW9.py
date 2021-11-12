# Import Libraries
import scipy.constants as sp
import math

# Variables

r_coil = 0.02
N_coil = 11
current = 7
velocity = 3.2
distance = 0.15
time = 0.0000001

# Calculations

area_coil = sp.pi * (r_coil**2)
b_i = ((sp.mu_0/(4*sp.pi)) * 2 * current)/(distance)
b_f = ((sp.mu_0/(4*sp.pi)) * 2 * current)/(distance - velocity * time)
dBdt = (b_f - b_i)/time
vm_reading = dBdt * area_coil * N_coil

# Print

print("Part 1: The magnitude of dB/dt in the coil =", dBdt, "T/s")
print("Part 2: The magnitude of the volmeter reading =", vm_reading, "V")
