# Import Libraries
import numpy as np
from scipy import constants
import math

# Variables
Q1 = 6E-8
Q2 = 3E-7
area = 2.6
disk_thickness = 0.00002
D1D2_dist = 0.004
D2D3_dist = 0.0017

# Calculations
E_12 = Q1/area/constants.epsilon_0
E_23 = Q2/area/constants.epsilon_0
dV_BC = -E_12 * D1D2_dist * math.cos(0)
dV_CD = -0 * disk_thickness * math.cos(0)
dV_DF = -E_23 * -D2D3_dist * math.cos(0)
dV_FG = -0 * disk_thickness * math.cos(0)
dV_AG = dV_BC + dV_DF
dU = dV_AG * -constants.e
dK = -dU

# Print
print("Electric field between D1 and D2:", E_12, "V/m")
print("VC-VB =", dV_BC, "V")
print("VD-VC =", dV_CD, "V")
print("VF-VD =", dV_DF, "V")
print("VG-VF =", dV_FG, "V")
print("VG-VA =", dV_AG, "V")
print("Potential energy of system:", dU, "J")
print("Kinetic energy of electron:", dK, "J")
