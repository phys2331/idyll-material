# Import Libraries
from scipy import constants

# Variables
cap = 1.5
v = 1.5

# Calculate
Q = cap*2*v
elec_num = abs(Q/-constants.e)

# Print
print("The charge on each plate is", Q, "C")
print("There are", elec_num, "excess electrons.")
