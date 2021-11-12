# Import Libraries

import numpy as np
from scipy import constants

# Constants

proton_charge = constants.elementary_charge
k = 1/(4*np.pi*constants.epsilon_0)

# First Way

proton_loc = np.array([0,0,0])
electron_loc = np.array([0, 0, -0.5*10**-10])
r_vec = electron_loc - proton_loc
r_vec_mag = np.linalg.norm(r_vec)
r_hat = r_vec/r_vec_mag

E_field = (k*proton_charge)/(np.abs(r_vec_mag)**2)
E_field_mag = np.linalg.norm(E_field)

print("First way answer:", "{:e}".format(E_field_mag))

# Second Way

r = 0.5*10**-10

E_field2 = np.abs((k*proton_charge)/(np.abs(r)**2))

print("Second way answer:", "{:e}".format(E_field2))
