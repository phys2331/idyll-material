# Import Libraries
from scipy import constants

# Variables
l = 0.55
w = 0.21
gap = 0.00032

# Calculate
C = (constants.epsilon_0 * l * w) / gap

# Print
print("The capacitance is", C, "F")
