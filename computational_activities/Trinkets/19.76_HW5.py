#Import Libraries
from scipy import constants
import math

# Variables
l = 0.1
w = 0.02
gap = 0.001
V_i = 100
R = 950
V_f = 55

# Calculate
area = l*w
C = (area*constants.epsilon_0)/gap
t = abs(math.log(abs((V_f/V_i)-1))*R*C)

# Print
print("It takes", t, "s")
