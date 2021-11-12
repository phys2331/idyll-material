# Import Libraries
from scipy import constants

# Variables
I = 0.263

# Calculations
molecules = 0.5*constants.Avogadro
elec_per_sec = I * 6.242*10**18
min = 60 #seconds
hour = 60 #minutes
hours = molecules/elec_per_sec/(min*hour)

# Print
print("The batteries will keep it lit", hours, "hours")
