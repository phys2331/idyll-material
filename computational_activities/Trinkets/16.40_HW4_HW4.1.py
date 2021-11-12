# Import Libraries
from scipy import constants
import math

# Variables
V = 14500
e_mass = constants.electron_mass
e_charge = -constants.e

#Calculate
velocity = math.sqrt((-2 * e_charge * V)/e_mass)

#Print
print("The velocity is", velocity, "m/s")
