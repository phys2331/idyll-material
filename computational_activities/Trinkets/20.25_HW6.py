# Import Libraries
import numpy as np
from scipy import constants
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

# Variables
v = np.array([0, 0, -8E5])
B = np.array([-0.37, 0, 0])
q = constants.e

# Calculate
F_mag = np.linalg.norm(np.cross(q*v, B))
F_mag_vec = np.cross(q*v, B)

# Print
print(F_mag)
print(F_mag_vec)

# Graph
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.set_xlim([-5E-15, 5E-15])
ax.set_ylim([-5E-15, 5E-15])
ax.set_zlim([-5E-15, 5E-15])
ax.set_xlabel('X', color = 'green')
ax.set_ylabel('Y', color = 'green')
ax.set_zlabel('Z', color = 'green')

ax.quiver(0, 0, 0, B[0], B[1], B[2], color='blue', label = B, arrow_length_ratio = .5)
ax.quiver(0, 0, 0, q*v[0], q*v[1], q*v[2], color='green', label = q*v, arrow_length_ratio = .5)
ax.quiver(0, 0, 0, F_mag_vec[0], F_mag_vec[1], F_mag_vec[2], color='red', label = F_mag_vec, arrow_length_ratio = .5)
plt.legend(loc = 2)
plt.show()
