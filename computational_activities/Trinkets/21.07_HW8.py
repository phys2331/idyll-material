# Import Libraries
import math
import numpy as np
from scipy import constants

# Variables
H = 0.03
W = 0.02
L = 0.08
E1 = 200
E2 = 1030

# Flux per side
flux_left = E1 * H * W * math.cos(np.pi)
flux_right = E2 * H * W * math.cos(0)
flux_top = E1 * L * W * round(math.cos(np.pi/2))
flux_bottom = E1 * L * W * round(math.cos(np.pi/2))
flux_front = E1 * L * H * round(math.cos(np.pi/2), 5)
flux_back = E1 * L * H * round(math.cos(np.pi/2), 5)

# Total Flux and Charge
flux_tot = flux_left + flux_right + flux_top + flux_bottom + flux_front + flux_back
q = flux_tot * constants.epsilon_0

# Print

print("Flux through the top =", flux_top, "Vm")
print("Flux through the bottom =", flux_bottom, "Vm")
print("Flux through the left =", flux_left, "Vm")
print("Flux through the right =", flux_right, "Vm")
print("Flux through the front =", flux_front, "Vm")
print("Flux through the back =", flux_back, "Vm")
print("The total flux =", flux_tot, "Vm")
print("The total charge inside =", q, "C")
