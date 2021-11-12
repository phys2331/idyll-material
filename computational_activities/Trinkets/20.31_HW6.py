# Import Libraries
from scipy import constants

# Variables
B = 0.16
w = 0.22
d = 0.01
q = constants.e
m = constants.value(u'atomic mass constant')

# Calculate
dV1_12 = ((w/2)**2*q*B**2)/(2*12*m)
dV2_12 = ((w/2)*q*B**2*d)/(12*m)
dV1_14 = ((w/2)**2*q*B**2)/(2*14*m)
dV2_14 = ((w/2)*q*B**2*d)/(14*m)

# Print
print(dV1_12)
print(dV2_12)
print(dV1_14)
print(dV2_14)
