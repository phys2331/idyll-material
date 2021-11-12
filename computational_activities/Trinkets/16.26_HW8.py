#Import Libraries
import numpy as np

#Variables
loc_i = np.array([1,6,8])
loc_f = np.array([4,8,13])
E = np.array([900,200,-460])

#Calculations
V_i = -np.dot(E, loc_i)
V_f = -np.dot(E, loc_f)
dV = V_f - V_i

#Print
print(dV)
