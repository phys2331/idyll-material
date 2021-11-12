# Import Libraries
import numpy as np

# Vectors
v_vec = np.array([432, -393, 336])
r_vec = np.array([0.577, 0.577, -0.577])

# Cross v_vec and r_hat
vr = np.cross(v_vec, r_vec)

# Print
print(vr)
