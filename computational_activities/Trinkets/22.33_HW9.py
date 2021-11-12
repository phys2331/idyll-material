#Import Libraries
import numpy as np
from scipy import constants

#Variables
dp = np.array([0,0,3])
v = np.array([0,0,8])
mag_cent = np.array([1,3,3])
loc = np.array([1.09,3,4])
t = 1E-15

#Calculations
area_flux = np.pi*(loc[0]-mag_cent[0])**2
vt = v * t
cent2 = vt + mag_cent
mu = constants.mu_0/(4*np.pi)
r1 = loc - mag_cent
r2 = loc - cent2
rmag1 = np.linalg.norm(r1)
rmag2 = np.linalg.norm(r2)
B_init = ((mu*2)/(rmag1**3))*dp
B_fin = ((mu*2)/(rmag2**3))*dp
phi_init = B_init * area_flux
phi_fin = B_fin * area_flux
delta_phi = phi_fin - phi_init
E = -delta_phi/(t * np.pi * 2 * r1[0])
E_field = np.array([0,E[2],0])

#Print
print("The electric field =", E_field, "N/C")
