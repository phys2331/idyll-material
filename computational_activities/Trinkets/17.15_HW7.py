# Import Libraries
import numpy as np
import math

# Variables
C_mag = 4
D_mag = 9
theta = 40

# Cross C x D part 1
CD = C_mag * D_mag * math.sin(math.radians(theta))

# Cross C x D part 2
C_vec = np.array([4, 0, 0])
D_opp = D_mag * math.sin(math.radians(theta))
D_adj = math.sqrt(D_mag**2 - D_opp**2)
D_vec = np.array([D_adj, D_opp, 0])
CD_vec = np.cross(C_vec, D_vec)

# Cross D x C
DC_vec = np.cross(D_vec, C_vec)

# Print answers
print(CD)
print(CD_vec)
print(DC_vec)
