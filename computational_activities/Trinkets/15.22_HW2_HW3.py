import numpy as np
from scipy import constants

rod_length = 1.8
rod_charge = -8*10**-8
A_loc = np.array([0.7,0,0])

origin = np.array([0,0,0])
k = 1/(4*np.pi*constants.epsilon_0)

piece_length = rod_length / 8
piece_5_center = np.array([0, origin[1]-(0.5*piece_length), 0])
piece_5_charge = rod_charge/8

r_vec = A_loc - piece_5_center
r_hat = r_vec / np.linalg.norm(r_vec)
E = k * (piece_5_charge/(np.linalg.norm(r_vec)**2)) * r_hat


print("The length of one piece is", piece_length, "m")
print("The center of piece number 5 is", list(piece_5_center), "m")
print("The charge on piece number 5 is", piece_5_charge, "C")
print("The electric field at A is", list(E), "N/C")
