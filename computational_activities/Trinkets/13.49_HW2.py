# Import Libraries

import numpy as np
from scipy import constants

# Constants

d = 400*10**-9
r = 128*10**-9
k = 1/(4*np.pi*constants.epsilon_0)
proton_charge = constants.elementary_charge
electron_charge = -constants.elementary_charge

# Locations

origin = np.array([0,0,0])
Cl_loc = np.array([0,0,0])
Fe_loc = np.array([Cl_loc[0] - d, 0, 0])
A_loc = np.array([Cl_loc[0] - r, 0, 0])
B_loc = np.array([Cl_loc[0] + r, 0, 0])

# E_A magnitude and direction

FeA_r_vec = A_loc - Fe_loc
FeA_r_hat = FeA_r_vec / np.linalg.norm(FeA_r_vec)
E_FeA = k * ((3 * proton_charge)/((d-r)**2)) * FeA_r_hat
ClA_r_vec = A_loc - Cl_loc
ClA_r_hat = ClA_r_vec / np.linalg.norm(ClA_r_vec)
E_ClA = k * (electron_charge)/((r)**2) * ClA_r_hat
E_Anet_vec = E_FeA + E_ClA
E_Anet_mag = np.linalg.norm(E_Anet_vec)

# E_B magnitude and direction

FeB_r_vec = B_loc - Fe_loc
FeB_r_hat = FeB_r_vec / np.linalg.norm(FeB_r_vec)
E_FeB = k * ((3 * proton_charge)/((d+r)**2)) * FeB_r_hat
ClB_r_vec = B_loc - Cl_loc
ClB_r_hat = ClB_r_vec / np.linalg.norm(ClB_r_vec)
E_ClB = k * (electron_charge)/((r)**2) * ClB_r_hat
E_Bnet_vec = E_FeB + E_ClB
E_Bnet_mag = np.linalg.norm(E_Bnet_vec)

# Force of electron at A

F_vec = electron_charge * E_Anet_vec
F_mag = np.linalg.norm(F_vec)


# Print

print("The magnitude at location A is", E_Anet_mag, "N/C")
if E_Anet_vec[0] < 0:
  print("The direction of E_B is to the left")
else:
  print("The direction of E_B is to the right")
print("The magnitude at location B is", E_Bnet_mag, "N/C")
if E_Bnet_vec[0] < 0:
  print("The direction of E_B is to the left")
else:
  print("The direction of E_B is to the right")
print("The magnitude of the force at A is", F_mag, "N")
if F_vec[0] < 0:
  print("The direction of the force is to the left")
else:
  print("The direction of the force is to the right")
