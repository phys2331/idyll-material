## Import Libraries
from scipy import constants

## Variables
L = 0.17
H = 0.04
W = 0.008
V1 = -0.45
V2 = 0.00029
B = 1.3
I = 0.4

# Calculate drift speed
ds = V2/(H*B)

# Calculate mobility of the mobile charges
E_length = abs(V1/L)
u = ds/E_length

# Amount of charges
n = I/(constants.e*H*W*ds)

# Resistance of the bar
R = abs(V1/I)

# Print answers

print("The drift speed is", ds, "m/s")
print("The mobility is", u, "m/s/V/m")
print("The amount of charges is", n, "mobile charges")
print("The resistance is", R, "ohms")
