# Import Libraries
import numpy as np
from scipy import constants

# Given variables and constants

tape_length = 0.11
tape_charge = 8*10**-9
A_loc = np.array([0,0.07,0])
origin = np.array([0,0,0])
k = 1/(4*np.pi*constants.epsilon_0)

# Lengths and charges of each piece

section_length = tape_length / 3
piece1_center = np.array([origin[0] - section_length,0,0])
piece2_center = origin
piece3_center = np.array([origin[0] + section_length,0,0])
section_charge = tape_charge / 3

# Electric field due to piece 1

piece1_r_vec = A_loc - piece1_center
piece1_r_hat = piece1_r_vec / np.linalg.norm(piece1_r_vec)
E1 = k * (section_charge / (np.linalg.norm(piece1_r_vec)**2)) * piece1_r_hat

# Electric field due to piece 2

piece2_r_vec = A_loc - piece2_center
piece2_r_hat = piece2_r_vec / np.linalg.norm(piece2_r_vec)
E2 = k * (section_charge / (np.linalg.norm(piece2_r_vec)**2)) * piece2_r_hat

# Electric field due to piece 3

piece3_r_vec = A_loc - piece3_center
piece3_r_hat = piece3_r_vec / np.linalg.norm(piece3_r_vec)
E3 = k * (section_charge / (np.linalg.norm(piece3_r_vec)**2)) * piece3_r_hat

# Net Electric Field

E_net = E1 + E2 + E3

# Print

print("The electric field due to piece 1 is", list(E1), "N/C")
print("The electric field due to piece 2 is", list(E2), "N/C")
print("The electric field due to piece 3 is", list(E3), "N/C")
print("The net electric field is", list(E_net), "N/C")
