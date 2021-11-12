# Import Libraries
import numpy as np
from scipy import constants

# Variables
r = 6.2
s = 0.0013
Q = 5.1*10**-4

# Calculate
area = np.pi*r**2
E = (Q/area)/constants.epsilon_0
num2_loc = s/2
V = E * num2_loc

# Conditions
if E and s > 0 or E and s < 0 :
  V_ans = -V
else:
  V_ans = V

# Print
print(V_ans)

# Version 2
# Import Libraries
import numpy as np
from scipy import constants

# Variables
r = 6.2
s = np.array([0.0013, 0, 0])
t = np.array([0.0005, 0, 0])
Q = 5.1*10**-4

# Calculations
loc_1 = t/2
loc_2 = s/2
E_loc1 = np.array([0,0,0])
E_loc2 = (Q/(np.pi*r**2))/constants.epsilon_0
V1 = -np.dot(E_loc1, loc_1)
V2 = -np.dot(E_loc2, loc_2)
dV = V2 - V1

# Print
print(dV, "V")
