# Import Libraries
import numpy as np
from scipy import constants

# Variables
r = 4.2
Q = 70*10**-6
s1 = 0.0017
s2 = 0.0006

# Coordinates
B = np.array([0, 0, 0])
A = np.array([s1, 0, 0])
C = np.array([0, -s2, 0])
D = np.array([s1, -s2, 0])

# Part 1
disk_area = np.pi*(r**2)
E = (Q/disk_area)/constants.epsilon_0

# Part 2
dl_BA = B-A
dl_CB = C-B
dl_CA = C-A
V_BA = E*abs(dl_BA[0])
V_CB = E*abs(dl_CB[0])
V_CA = E*abs(dl_CA[0])

# Part 3
lcos = V_CA/E

# Print
print("Part 1")
print("The electric field is", E, "N/C")
print("Part 2")
print("VB-VA is", V_BA, "V")
print("VC-VB is", V_CB, "V")
print("VC-VA is", V_CA, "V")
print("Part 3")
print("Lcos is", lcos, "m")
print("VC-VA is", V_CA, "V")
