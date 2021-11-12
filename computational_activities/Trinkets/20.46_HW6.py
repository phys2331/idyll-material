# Import Libraries
import numpy as np
from scipy import constants

# Variables
v = np.array([5E5, 0, 0])
B = np.array([0, 0.6, 0])
q = -constants.e

# Calculations
F_B = np.cross(q*v, B)
F_E = -F_B
E = F_E/q

# Print
print(F_B)
print(F_E)
print(E)
