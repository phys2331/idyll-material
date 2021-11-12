# Import Libraries
import numpy as np
from scipy import constants

# Variables
r = 4.2
s = 0.002
Q = 45*10**-6
s1 = 0.0014
s2 = 0.0006

# Coordinates
B = np.array([0, 0, 0])
A = np.array([s1, 0, 0])
C = np.array([0, -s2, 0])
D = np.array([s1, -s2, 0])

# Part 1 Calculations
disk_area = np.pi*(r**2)
E = np.array([(Q/disk_area)/constants.epsilon_0, 0, 0])

# Part 2 Calculations
dl_BA = B-A
V_BA = np.linalg.norm(E)*abs(dl_BA[0])

# Part 3 Calculations
dl_CB = C-B
V_CB = np.linalg.norm(E)*abs(dl_CB[0])

# Part 4 Calculations
dl_AC = A-C
V_AC = np.linalg.norm(E)*-dl_AC[0]

# Print
print("Part 1")
print("The electric field inside the capacitor is", list(E), "N/C")
print("Part 2")
print("dl along the path is", list(dl_BA), "m")
