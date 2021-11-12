# Import Libraries
import numpy as np
from scipy import constants

# Variables
I = 15
s = 0.003
d = 0.43

# Magnetic field magnitude
B = (constants.mu_0/(4*np.pi)) * I *((1/(d-(s/2)))-(1/(d+(s/2)))) * 2
B1 = (constants.mu_0/(4*np.pi)) * 2*I / (d-(s/2))
B2 = (constants.mu_0/(4*np.pi)) * 2*I / (d+(s/2))
B3 = B1-B2

# Print
print("The max magnetic field is", B, "T")
print(B3)
