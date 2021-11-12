
# Import Libraries
import numpy as np
from scipy import constants

# Given information
L = 1.5
seg = 8
A = np.array([0.093, 0.206, 0])
I = 8.2

# Segment calculations
seg_length = L/seg
seg_vec_init = np.array([seg_length*-2, 0, 0])
seg_vec_fin = np.array([seg_length*-1, 0, 0])
cent_seg = (seg_vec_init + seg_vec_fin)/2
dl_seg = seg_vec_fin-seg_vec_init
seg_vec_mag = np.linalg.norm(dl_seg)

# Calculate r_vec and r_hat
r_vec = A - cent_seg
r_hat = r_vec/np.linalg.norm(r_vec)

# Calculate dl cross r_hat
dlr = np.cross(dl_seg, r_hat)

# Calculate the magnetic field at observation location
dB = (constants.mu_0/(4*np.pi))* ((I * dlr) / np.linalg.norm(r_vec)**2)

# Print
print("Part 2: Segment # is", seg_length, "m")
print("Part 3: The magnitude of dl for a segment is", seg_vec_mag, "m")
print("Part 4: dl for a segment is", dl_seg, "m")
print("Part 5: The center of the segment is", cent_seg, "m")
print("Part 6: the r vector is", r_vec, "m")
print("Part 7: The unit vector is", r_hat)
print("Part 8: dl cross r_hat is", dlr, "m")
print("Part 9: The magnetic field is", dB, "T")
