# Import Libraries
import math
from scipy import constants
import numpy as np

# Variables
L = 0.075
d = 0.0216
I = 0.76
turns = 3
sides = 3
B_earth = 2E-5

# Magnetic field magnitude
B = (constants.mu_0/(4*np.pi))* (L*I)/(d * math.sqrt(d**2 + ((L/2)**2))) * sides * turns
B2 = (constants.mu_0/(4*np.pi))* (L*3*I)/(d * math.sqrt(d**2 + ((L/2)**2))) * turns
B3 = constants.mu_0/(4*np.pi)*L*I/(d * math.sqrt(d**2 + ((L/2)**2))) * sides * turns

B4 = (constants.mu_0)/4*np.pi))* (L*I)/(d * math.sqrt(d**2 + ((L/2)**2)))
B5 = constants.mu_0/(4*np.pi)*L*I/(d * math.sqrt(d**2 + ((L/2)**2)))

# Compass deflection
theta = math.degrees(math.atan(B/B_earth))

# Print
print("The magnetic field is", B, "T")
print("The deflection is", theta, "degrees")
print(B3)
print(B4)
print(B5)
