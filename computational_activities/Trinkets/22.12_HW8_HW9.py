#Import Libraries
import scipy.constants as sp
import math

#Variables
r_sol = .04
B_sol = 0.4

#Calculations
area_sol = sp.pi * r_sol**2
mag_flux = B_sol * area_sol * math.cos(0)

# Print
print("The flux through the outer ring =", mag_flux, "Tm^2")
