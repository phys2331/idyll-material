#Import Libraries
import math
import numpy as np

#Variables
r = 0.02
E = 278
theta = 44
nE_theta = 90 - theta

# Calculations
A = np.pi * (r**2)
E_flux = E * A * math.cos(math.radians(nE_theta))

# Print
print("The electric flux is", E_flux, "Vm")
