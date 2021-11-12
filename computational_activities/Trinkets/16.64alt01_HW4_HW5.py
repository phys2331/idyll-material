# Import Libraries
import numpy as np
from scipy import constants
import math

# Variables
E = 3*10**6
L = 0.77
r = 0.0008
R = 0.045
k = 1/(4*np.pi*constants.epsilon_0)

# Calculate
Q = L * (2* np.pi*constants.epsilon_0)*E*abs(r)
dV = abs(((2*Q*k)/L)*math.log(R/r))

# Print
print("The charge on the inner wire is", Q, "C")
print("The potential difference is", dV, "V")
